from transformers.configuration_utils import PretrainedConfig


class SarvamMLAConfig(PretrainedConfig):
    model_type = "sarvam_mla"

    base_model_pp_plan = {
        "embed_tokens": (["input_ids"], ["inputs_embeds"]),
        "layers": (["hidden_states", "attention_mask"], ["hidden_states"]),
        "norm": (["hidden_states"], ["hidden_states"]),
    }

    base_model_tp_plan = {
        "layers.*.self_attn.q_proj": "colwise",
        "layers.*.self_attn.kv_b_proj": "colwise",
        "layers.*.self_attn.o_proj": "rowwise",
    }

    def __init__(
        self,
        vocab_size: int = 262144,
        hidden_size: int = 4096,
        num_hidden_layers: int = 32,
        intermediate_size: int = 16384,
        moe_intermediate_size: int = 2048,
        num_experts: int = 128,
        num_experts_per_tok: int = 8,
        num_shared_experts: int = 1,
        first_k_dense_replace: int = 1,
        num_attention_heads: int = 64,
        qk_rope_head_dim: int = 64,
        qk_nope_head_dim: int = 128,
        kv_lora_rank: int = 512,
        v_head_dim: int = 128,
        max_position_embeddings: int = 4096,
        rope_theta: float = 10000.0,
        rope_scaling: dict = None,
        attention_dropout: float = 0.0,
        output_dropout: float = 0.0,
        rms_norm_eps: float = 1e-6,
        hidden_act: str = "silu",
        use_cache: bool = True,
        use_qk_norm: bool = True,
        moe_router_enable_expert_bias: bool = True,
        routed_scaling_factor: float = 2.5,
        output_router_logits: bool = False,
        tie_word_embeddings: bool = False,
        pad_token_id: int = 0,
        eos_token_id: int = 1,
        embedding_dropout: float = 0.0,
        initializer_range: float = 0.006,
        attn_implementation: str = "eager",
        **kwargs,
    ):
        # core geometry
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.intermediate_size = intermediate_size
        self.num_attention_heads = num_attention_heads
        self.max_position_embeddings = max_position_embeddings

        # MLA geometry
        self.qk_rope_head_dim = qk_rope_head_dim
        self.qk_nope_head_dim = qk_nope_head_dim
        self.kv_lora_rank = kv_lora_rank
        self.v_head_dim = v_head_dim
        # convenient derived dim
        self.q_head_dim = qk_rope_head_dim + qk_nope_head_dim
        # vLLM MLA expects "head size" = Lkv + R, not hidden_size/num_heads.
        self.head_dim = int(self.kv_lora_rank + self.qk_rope_head_dim)

        # MoE
        self.moe_intermediate_size = moe_intermediate_size
        self.num_experts = num_experts
        self.num_experts_per_tok = num_experts_per_tok
        self.num_shared_experts = num_shared_experts
        self.first_k_dense_replace = first_k_dense_replace

        # Router
        self.moe_router_enable_expert_bias = moe_router_enable_expert_bias
        self.routed_scaling_factor = routed_scaling_factor
        self.output_router_logits = output_router_logits

        # dropouts / norms / init
        self.attention_dropout = attention_dropout
        self.output_dropout = output_dropout
        self.embedding_dropout = embedding_dropout
        self.rms_norm_eps = rms_norm_eps
        self.initializer_range = initializer_range
        self.hidden_act = hidden_act

        # rope / cache
        self.rope_theta = rope_theta
        self.use_cache = use_cache
        self.use_qk_norm = use_qk_norm
        self.rope_scaling = rope_scaling
        self.default_theta = 10000.0

        if self.rope_scaling is None:
            self.rope_scaling = {
                'beta_fast': 32,
                'beta_slow': 1,
                'factor': 40,
                'mscale': 1.0,
                'mscale_all_dim': 1.0,
                'original_max_position_embeddings': 4096,
                'rope_type': 'deepseek_yarn',
            }

        self.attn_implementation = attn_implementation
        self._attn_implementation = attn_implementation

        if "_attn_implementation" in kwargs:
            self._attn_implementation = kwargs.pop("_attn_implementation")
            if hasattr(self, "attn_implementation"):
                self.attn_implementation = self._attn_implementation

        super().__init__(
            pad_token_id=pad_token_id,
            eos_token_id=eos_token_id,
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )

    def convert_rope_params_to_dict(self, ignore_keys_at_rope_validation: set | None = None, **kwargs):
        rope_scaling = kwargs.pop("rope_scaling", None)
        self.rope_parameters = rope_scaling or self.rope_parameters
        self.rope_parameters = self.rope_parameters if self.rope_parameters is not None else {}

        # Standardize and validate the correctness of rotary position embeddings parameters
        self.rope_parameters.setdefault("rope_theta", kwargs.pop("rope_theta", self.default_theta))
        self.standardize_rope_params()
        self.validate_rope(ignore_keys=ignore_keys_at_rope_validation)

        # Convert to float because RoPE fn expect a float. Models on the hub were saved as int
        for key in ["beta_fast", "beta_slow", "factor"]:
            if key in self.rope_parameters:
                self.rope_parameters[key] = float(self.rope_parameters[key])
        return kwargs