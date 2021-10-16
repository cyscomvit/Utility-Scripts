# Certificate Generation

### Setup the Certificate Generation

1. Add the template certificate named `certificate.png` in the `/CertificateGeneration` directory
2. Add the csv file named `list.csv` in the same `/CertificateGeneration` directory
3. Change the positioning and font size accordingly in the `main.py` [here](https://github.com/owaspvit/utility-scripts/blob/74caf52294a7f7528195c31fbdb6c215091413bd/certificategeneration/main.py#l10)

### Commands to setup the env for certificate Generation

    cd \CertificateGeneration
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python .\main.py
