####################################################################
#
#  Makefile for INGI2141 QCM
#  OB, Jan 2013
#
####################################################################

QCM=1

EXNAME=../html/qcm$(QCM).html

RST_FILES=Qcm-network-$(QCM).rst

CSS=../rst-form/css/html4css1.css,../rst-form/css/rst-form.css,../rst-form/css/pygments.css

.PHONY : qcm all

qcm: $(EXNAME)

$(EXNAME): $(RST_FILES)
	@for i in $(RST_FILES); do\
	( rst2html.py --stylesheet-path=$(CSS)  $$i > $(EXNAME) ; ) ; done

all: qcm

clean:
	-rm -r $(EXNAME)
