# Certificate Generation

### Setup the Certificate Generation

1. Add the template certificate named `certificate.png` in the `/CertificateGeneration` directory
2. Add the csv file named `list.csv` in the same `/CertificateGeneration` directory
3. Change the positioning and font size accordingly in the `main.py` [here](https://github.com/owaspvit/Utility-Scripts/blob/7cff81cd093a67c0b769f2fa1090e589085b4c83/CertificateGeneration/main.py#L10)

### Commands to setup the env for certificate Generation

    cd \CertificateGeneration
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python .\main.py
