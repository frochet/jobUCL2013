###################################################################
#
#  Makefile for INGI2141 QCM
#  OB, Jan 2013
#
####################################################################

QCM=1

EXNAME=../html/qcm-lan-$(QCM).html

RST_FILES=Qcm-lan-$(QCM).rst

CSS=../rst-form/css/html4css1.css,../rst-form/css/rst-form.css,../rst-form/css/pygments.css

.PHONY : qcm all

qcm: $(EXNAME)

$(EXNAME): $(RST_FILES)
	@for i in $(RST_FILES); do\
	( rst2html.py --stylesheet-path=$(CSS)  $$i > $(EXNAME) ; ) ; done
all: qcm

clean:
	-rm -r $(EXNAME)
