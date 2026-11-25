<h1 align="center">Convert tractmeasures to tractprofile</h1>

<p align="center">
  One tract-profile CSV per tract, in the deprecated tractprofile format, from a tractmeasures table that holds all tracts.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.524"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.524-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts a tractmeasures CSV (all tracts in one table) into the deprecated tractprofile format with one profile CSV per tract, using pandas.**

Utility that splits the tractmeasures table by structureID and writes one <tract>_profiles.csv per tract without the subject, structure and node ID columns. Use it only to feed Apps that still require the deprecated tractprofile datatype.

| | |
|---|---|
| **Inputs** | `neuro/tractmeasures` |
| **Outputs** | `neuro/tractprofile-deprecated` |
| **Container** | `brainlife/freesurfer-stats:1.2` |
| **Resources** | 1 CPUs · 0.17 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.524](https://doi.org/10.25663/brainlife.app.524) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `tractmeasures` | `neuro/tractmeasures` | yes | Tract profiles table (tractmeasures.csv) with subjectID, structureID and nodeID columns. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `profiles` | `neuro/tractprofile-deprecated` | Directory with one <tract>_profiles.csv per tract (tractprofile format). |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.524](https://doi.org/10.25663/brainlife.app.524), choose a `neuro/tractmeasures` dataset and press **Execute**. The App writes a `neuro/tractprofile-deprecated` dataset to your project.

This App is designed for use within brainlife.io: it splits a concatenated tractmeasures table, which contains the profiles of all the tracts in a white matter classification, into a single CSV per tract. Use it only to feed Apps that still require the deprecated tractprofile datatype.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/). The App runs in the `brainlife/freesurfer-stats:1.2` container (Python 3 with pandas).

1. Clone this repository and check out the released version (`git checkout v1.1`).
2. Create `config.json` with the path to your tractmeasures table:

   ```json
   {
       "tractmeasures": "/input/tractmeasures/tractmeasures.csv"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

### Sample data

You can download sample datasets from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset-id>
```

## Outputs

```text
profiles/
├── <tract>_profiles.csv   one file per structureID in the input table
└── …
```

Each file holds the profile measures of one tract; the `subjectID`, `structureID` and `nodeID` columns of the input table are dropped.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Convert tractmeasures datatype to tractprofile datatype. brainlife.io App. [doi:10.25663/brainlife.app.524](https://doi.org/10.25663/brainlife.app.524)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## Authors

- Brad Caron
- Franco Pestilli (project director)

**Contributors:** Soichi Hayashi

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](LICENSE).
