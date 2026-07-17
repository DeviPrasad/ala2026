numpy:
	xelatex --shell-escape np00.tex
	open np00.pdf

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
