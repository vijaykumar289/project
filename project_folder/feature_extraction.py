import re

def extract_features(url):
    features = []
    # Length of URL
    features.append(len(url))
    
    # Number of dots in URL
    features.append(url.count('.'))
    
    # Presence of "@" symbol
    features.append(1 if '@' in url else 0)
    
    # Presence of "-" symbol
    features.append(1 if '-' in url else 0)
    
    # Presence of "https"
    features.append(1 if url.startswith('https') else 0)
    
    # Number of subdomains
    features.append(len(re.findall(r'\.', url.split('//')[-1])) - 1)
    
    # Length of domain name
    domain = re.findall(r'://([^/]+)', url)
    if domain:
        features.append(len(domain[0]))
    else:
        features.append(0)
    
    # Presence of IP address in URL
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)
    
    return features
