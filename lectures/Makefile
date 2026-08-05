intro:
	xelatex --shell-escape intro.tex
	open intro.pdf

vec-questions:
	xelatex --shell-escape vec-questions.tex
	open vec-questions.pdf

vector-spaces:
	xelatex --shell-escape vec-spaces.tex
	open vec-spaces.pdf

linear-functions:
	xelatex --shell-escape linear-functions.tex
	open linear-functions.pdf

norm-dist:
	xelatex --shell-escape norm-dist-std.tex
	open norm-dist-std.pdf

np:
	xelatex --shell-escape np00.tex
	open np00.pdf

ndarray:
	xelatex --shell-escape ndarray.tex
	open ndarray.pdf

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
