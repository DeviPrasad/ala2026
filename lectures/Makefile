intro:
	latexmk -xelatex --shell-escape intro.tex
	open intro.pdf

affine:
	latexmk -xelatex --shell-escape affine.tex
	open affine.pdf

vec-angle-proof:
	latexmk -xelatex vector-angle-proof.tex
	open vector-angle-proof.pdf

vec-questions:
	latexmk -xelatex --shell-escape vec-questions.tex
	open vec-questions.pdf

vector-spaces:
	latexmk -xelatex --shell-escape vec-spaces.tex
	open vec-spaces.pdf

linear-functions:
	latexmk -xelatex --shell-escape linear-functions.tex
	open linear-functions.pdf

norm-dist:
	latexmk -xelatex --shell-escape norm-dist-std.tex
	open norm-dist-std.pdf

matrix-vec:
	latexmk -xelatex --shell-escape matrix-vec-linear.tex
	open matrix-vec-linear.pdf

np:
	latexmk -xelatex --shell-escape np00.tex
	open np00.pdf

ndarray:
	latexmk -xelatex --shell-escape ndarray.tex
	open ndarray.pdf

knn:
	latexmk -xelatex knn-example.tex
	latexmk -xelatex knn-house-price.tex
	open knn-house-price.pdf

all: numpy
	echo "Done!"

copy-my-mint-style:
	cp mymint.py ../src/linalg/lib/python3.12/site-packages/pygments/styles/mymint.py
	cp mymint.py /usr/local/lib/python3.11/site-packages/pygments/styles/mymint.py

mint-style:
	sudo python -m pygments.cmdline -S mymint -f latex

clean:
	@rm -f *.aux *.log *.snm *.out *.toc *.nav *.vrb
	@rm -rf _minted *.message.minted
