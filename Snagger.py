import requests
import configparser
import threading
from queue import Queue

# Load configuration file
config = configparser.ConfigParser()
config.read('snagger_config.ini')

# Extract settings from the configuration
site_number = int(config.get('site', 'siteNum'))
custom_url_template = config.get('site', 'customSite')
output_file = config.get('lists', 'output')
wordlist_file = config.get('lists', 'wordList')
enable_proxy = config.getboolean('proxy', 'enableProxy')
proxy_list_file = config.get('proxy', 'proxyList')
thread_count = int(config.get('multithreading', 'threadCount'))

# Define social media URL templates
url_templates = {
    3: "https://twitter.com/{}",
    4: "https://instagram.com/{}",
    12: "https://youtube.com/{}",
    14: "https://facebook.com/{}",
    15: "https://linkedin.com/in/{}",
    16: "https://tiktok.com/@{}",
    17: "https://snapchat.com/add/{}",
    18: "https://reddit.com/user/{}",
    19: "https://pinterest.com/{}",
    20: "https://discord.com/users/{}",
    # Add more platforms as needed
}

def load_proxies():
    proxies = []
    if enable_proxy:
        with open(proxy_list_file, 'r') as f:
            proxies = [{'http': f"http://{proxy.strip()}", 'https': f"https://{proxy.strip()}"} for proxy in f.readlines()]
    return proxies

def check_username(username, proxy=None):
    if site_number == 1:
        url = custom_url_template.replace('%%word%%', username)
    else:
        url_template = url_templates.get(site_number, custom_url_template)
        url = url_template.format(username)

    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        if response.status_code == 404:
            return username, True
    except requests.RequestException:
        return username, False
    return username, False

def worker(queue, proxies):
    while not queue.empty():
        username = queue.get()
        proxy = None
        if proxies:
            proxy = proxies[queue.qsize() % len(proxies)]
        result, available = check_username(username, proxy)
        if available:
            with threading.Lock():
                with open(output_file, 'a') as file:
                    file.write(f"{result}\n")
        queue.task_done()

def main():
    # Load proxies
    proxies = load_proxies()

    # Load word list
    queue = Queue()
    with open(wordlist_file, 'r') as file:
        for line in file:
            queue.put(line.strip())

    # Start threads
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(queue, proxies))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Username checking complete. Available usernames written to", output_file)

if __name__ == "__main__":
    main()
