# Create a dict of accept headers for each user-agent.
accepts = {"Firefox": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Safari, Chrome": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5"}

# Get a random user-agent. We used Chrome and Firefox user agents.
# Getting a user agent using the fake_useragent package
ua = UserAgent()
random_user_agent = ua.chrome if random.random() > 0.5 else ua.firefox
valid_accept = accepts['Firefox'] if random_user_agent.find('Firefox') > 0 else accepts['Safari, Chrome']
headers = {"User-Agent": random_user_agent,
          "Accept": valid_accept}

# See below for the complete function