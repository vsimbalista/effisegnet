
# EffiSegNet - Actinic Cheilitis

This repository contains a modified version of the [EffiSegNet](https://github.com/ivezakis/effisegnet) architecture originally developed by **Ioannis Vezakis**. The original work proposes a lightweight, efficient semantic segmentation network based on EfficientNet and GhostModules.

This fork includes adaptations and modifications made for academic purposes as part of an undergraduate thesis project at [UNIFESP](https://unifesp.br/campus/sjc/).
For this work, the EffiSegNet model was applied in a new dataset, and the code has been restructured to use K-Fold Cross Validation.

## Paper
Under review.

## Original Work

[![GitHub](https://img.shields.io/badge/GitHub-ivezakis/effisegnet-black)](https://github.com/ivezakis/effisegnet)

[![arXiv](https://img.shields.io/badge/arXiv-2407.16298-b31b1b.svg)](https://arxiv.org/abs/2407.16298) 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10601024.svg)](https://doi.org/10.5281/zenodo.10601024)

## Changes in This Version

- Changed previous validation pipeline to a 10-fold cross-validation
- New dataset with Actinic Cheilitis images
- Modified training loop to include additional performance metrics (IoU, F1-Score)
- Organized results and metrics export to `.json` and `.xlsx`
- Added miscellaneous tests and scripts
- Added many many comments in Portuguese (to help me and my colleagues interpret the general logic in the scripts)

## Dataset

The dataset used in this project is composed of a collection of digital photographs of Actinic-Cheilitis-afflicted lips and their corresponding ground truth inflammation segmentation masks. The dataset is not currently available for public use.

## Citation

If you use this work or the modified version in your research, please cite the original paper:

```bibtex
@misc{vezakis2024effisegnetgastrointestinalpolypsegmentation,
      title={EffiSegNet: Gastrointestinal Polyp Segmentation through a Pre-Trained EfficientNet-based Network with a Simplified Decoder}, 
      author={Ioannis A. Vezakis and Konstantinos Georgas and Dimitrios Fotiadis and George K. Matsopoulos},
      year={2024},
      eprint={2407.16298},
      archivePrefix={arXiv},
      primaryClass={eess.IV},
      url={https://arxiv.org/abs/2407.16298}, 
}
```

---

> ⚠️ This project is a modified academic version and is not affiliated with the original author.
