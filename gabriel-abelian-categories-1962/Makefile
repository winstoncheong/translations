# Build the English translation of Gabriel (1962).
#
#   make          compile to build/main.pdf
#   make report   show translation progress
#   make strict   fail if French text or TODO markers remain
#   make clean    remove build artefacts
#
# The same commands are what CI runs (see ../../.github/workflows/ci.yml).

SRC    := src
BUILD  := build
TARGET := $(BUILD)/main.pdf

LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: all report strict clean

all: $(TARGET)

$(TARGET):
	cd $(SRC) && $(LATEXMK) -outdir=../$(BUILD) main.tex

report:
	cd ../.. && python tools/translation_report.py . --format text

strict:
	cd ../.. && python tools/translation_report.py . --strict

clean:
	latexmk -C -outdir=../$(BUILD) $(SRC)/main.tex
	rm -rf $(BUILD)