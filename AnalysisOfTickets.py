problems = [
    {
        "problem": "Laptop won't turn on",
        "cause": "Battery issue, AC adapter issue, Motherboard failure",
        "troubleshooting": [
            "Check if the battery is charged",
            "Try a different AC adapter",
            "Ensure power outlet is functioning"
        ],
        "resolution": [
            "Charge the battery",
            "Replace the AC adapter",
            "Seek professional repair for motherboard"
        ]
    },
    {
        "problem": "Screen is blank",
        "cause": "Brightness level, External display settings, Graphics card issue",
        "troubleshooting": [
            "Increase the screen brightness",
            "Check if laptop is in external display mode",
            "Restart the laptop"
        ],
        "resolution": [
            "Adjust brightness settings",
            "Switch from external display mode to laptop screen mode",
            "Update graphics card drivers or seek professional repair"
        ]
    },
    {
        "problem": "Laptop is overheating",
        "cause": "Blocked vents, Old thermal paste, Malware or excessive processes running",
        "troubleshooting": [
            "Check for blockages in the cooling vents",
            "Monitor CPU and memory usage",
            "Ensure laptop is on a hard surface"
        ],
        "resolution": [
            "Clean the cooling vents",
            "Update or scan for malware",
            "Replace thermal paste or seek professional repair"
        ]
    },
    {
        "problem": "Laptop is slow",
        "cause": "Low RAM, Old HDD, Too many background processes, Malware",
        "troubleshooting": [
            "Check RAM usage",
            "Monitor disk activity",
            "Review startup programs"
        ],
        "resolution": [
            "Upgrade RAM",
            "Replace HDD with SSD",
            "Disable unnecessary startup programs, Scan for malware"
        ]
    },
    {
        "problem": "Sound isn't working",
        "cause": "Muted volume, Corrupted drivers, Hardware issue",
        "troubleshooting": [
            "Check if volume is muted",
            "Verify sound device in sound settings",
            "Reinstall sound drivers"
        ],
        "resolution": [
            "Unmute volume or adjust volume settings",
            "Set the correct sound device as default",
            "Seek professional repair if hardware issue suspected"
        ]
    }
]

problems.extend([
    {
        "problem": "Keyboard or specific keys not working",
        "cause": "Dirt or debris under the keys, Hardware malfunction, Software driver issues",
        "troubleshooting": [
            "Check if external keyboards work",
            "Restart the laptop",
            "Inspect for visible debris under keys"
        ],
        "resolution": [
            "Clean the keyboard or specific key area",
            "Update or reinstall keyboard drivers",
            "Replace keyboard or seek professional repair"
        ]
    },
    {
        "problem": "Laptop suddenly shuts down",
        "cause": "Overheating, Faulty battery, Software errors",
        "troubleshooting": [
            "Check the temperature of the laptop",
            "Inspect for unusual software behaviors or error messages",
            "Try running the laptop directly on AC power"
        ],
        "resolution": [
            "Improve ventilation or clean internal fans",
            "Run software updates or system restore",
            "Replace the battery"
        ]
    },
    {
        "problem": "Wireless connection keeps dropping",
        "cause": "Weak Wi-Fi signal, Faulty laptop Wi-Fi card, Router issues",
        "troubleshooting": [
            "Check the strength of the Wi-Fi signal",
            "Try connecting to a different network or hotspot",
            "Restart the router and laptop"
        ],
        "resolution": [
            "Move closer to the router or eliminate physical obstructions",
            "Update wireless drivers",
            "Replace the laptop Wi-Fi card or consult with your ISP"
        ]
    },
    {
        "problem": "Touchpad not responsive",
        "cause": "Driver issues, External mouse interference, Hardware faults",
        "troubleshooting": [
            "Check if an external mouse works",
            "Ensure no external devices are interfering with the touchpad",
            "Update touchpad drivers"
        ],
        "resolution": [
            "Disconnect external mice and check again",
            "Reinstall or update touchpad drivers",
            "Seek professional repair"
        ]
    },
    {
        "problem": "Laptop battery drains quickly",
        "cause": "Old battery, Bright screen settings, Running resource-intensive applications",
        "troubleshooting": [
            "Check battery health in system settings",
            "Review running applications for high power consumption",
            "Lower screen brightness or turn off backlit keyboard"
        ],
        "resolution": [
            "Replace the battery",
            "Optimize application settings or close unnecessary apps",
            "Adjust power management settings"
        ]
    }
])

mail="""

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 10:14 AM
Subject: Urgent Assistance Needed with My Laptop

Hello Support Team,

I recently purchased a laptop from your store, and I'm encountering a couple of issues that are affecting my ability to use it effectively. 

Firstly, my laptop suddenly shuts down without any warning. I've noticed that it tends to get quite hot around the base, especially when I'm using resource-intensive applications. Secondly, the battery drains incredibly fast. Even with minimal usage, it doesn't last more than 2 hours.

Can you please help?

Thank you,
John Doe
----------------------------------------------------------------

----------------------------------------------------------------
From: support@laptopsolutions.com
To: john.doe@email.com
Date: Monday, 22 September 2023 12:30 PM
Subject: RE: Urgent Assistance Needed with My Laptop

Hello John,

Thank you for reaching out to us. We're sorry to hear about the issues you're experiencing with your laptop.

For the sudden shutdowns, it sounds like your laptop might be overheating, especially if it's getting hot. We recommend:
1. Ensuring the laptop is on a hard, flat surface for proper ventilation.
2. Regularly cleaning any dust or debris from the vents.
3. Avoiding running too many resource-intensive applications simultaneously.

Regarding the battery issue:
1. Check your screen brightness and lower it if set too high.
2. Turn off any unnecessary background applications.
3. Review your battery health in the system settings to see if it's deteriorating.

If these initial steps don't help, please get back to us, and we'll advise further.

Warm regards,
Laptop Solutions Support Team
----------------------------------------------------------------

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

Thank you for the quick response. I tried the suggestions you provided. The laptop still feels warm, but the shutdowns are less frequent. However, the battery still drains quickly even after reducing the brightness and closing background applications. 

Would it be best to bring it into your store for a professional check?

Regards,
John Doe
----------------------------------------------------------------

----------------------------------------------------------------
From: support@laptopsolutions.com
To: john.doe@email.com
Date: Monday, 22 September 2023 04:00 PM
Subject: RE: RE: RE: Urgent Assistance Needed with My Laptop

Hello John,

You're welcome. Given that you've tried the initial steps and are still experiencing battery issues, it might be best to bring the laptop into our store. We can have our technicians perform a thorough check to determine the root cause.

Please visit our store at your earliest convenience, and we'll assist further.

Best,
Laptop Solutions Support Team
----------------------------------------------------------------

"""
prompt = f"""

Given the customer email delimited by ```, \
Identify the last statement of the email and set the status to one of the following \
a.Cancelled b.open c.closed,d.Escalate e.check with logistics
Identify if the sentiment is negative \
Identify the topic not more than one.
Identify the problem statement,cause of problem,troubleshooting steps, if troubleshooted or not , status 
Customer Email: ```{mail}```
Json object: Key:(email,status,sentiment,topics,problem statement,cause of problem,troubleshooting steps, if troubleshooted or not)
"""
response = get_completion(prompt, temperature=0.7)
print(response)

mail="""

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 10:14 AM
Subject: Urgent Assistance Needed with My Laptop

Hello Support Team,

I recently purchased a laptop from your store, and I'm encountering a couple of issues that are affecting my ability to use it effectively. 

Firstly, my laptop suddenly shuts down without any warning. I've noticed that it tends to get quite hot around the base, especially when I'm using resource-intensive applications. Secondly, the battery drains incredibly fast. Even with minimal usage, it doesn't last more than 2 hours.

Can you please help?

Thank you,
John Doe
----------------------------------------------------------------

----------------------------------------------------------------
From: support@laptopsolutions.com
To: john.doe@email.com
Date: Monday, 22 September 2023 12:30 PM
Subject: RE: Urgent Assistance Needed with My Laptop

Hello John,

Thank you for reaching out to us. We're sorry to hear about the issues you're experiencing with your laptop.

For the sudden shutdowns, it sounds like your laptop might be overheating, especially if it's getting hot. We recommend:
1. Ensuring the laptop is on a hard, flat surface for proper ventilation.
2. Regularly cleaning any dust or debris from the vents.
3. Avoiding running too many resource-intensive applications simultaneously.

Regarding the battery issue:
1. Check your screen brightness and lower it if set too high.
2. Turn off any unnecessary background applications.
3. Review your battery health in the system settings to see if it's deteriorating.

If these initial steps don't help, please get back to us, and we'll advise further.

Warm regards,
Laptop Solutions Support Team
----------------------------------------------------------------

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

Thank you for the quick response. I tried the suggestions you provided. The laptop still feels warm, but the shutdowns are less frequent. However, the battery still drains quickly even after reducing the brightness and closing background applications. 

Would it be best to bring it into your store for a professional check?

Regards,
John Doe
----------------------------------------------------------------


"""

prompt = f"""

Given the customer email delimited by ```, \
Identify the last statement of the email and set the status to one of the following \
a.Cancelled b.open c.closed,d.Escalate e.check with logistics
Identify if the sentiment is negative \
Identify the topic not more than one.
Identify the problem statement,cause of problem,troubleshooting steps, if troubleshooted or not , status 
Customer Email: ```{mail}```
Json object: Key:(email,status,sentiment,topics,problem statement,cause of problem,troubleshooting steps, if troubleshooted or not)
"""
response = get_completion(prompt, temperature=0.7)
print(response)


mail="""

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 10:14 AM
Subject: Urgent Assistance Needed with My Laptop

Hello Support Team,

I recently purchased a laptop from your store, and I'm encountering a couple of issues that are affecting my ability to use it effectively. 

Firstly, my laptop suddenly shuts down without any warning. I've noticed that it tends to get quite hot around the base, especially when I'm using resource-intensive applications. Secondly, the battery drains incredibly fast. Even with minimal usage, it doesn't last more than 2 hours.

Can you please help?

Thank you,
John Doe
----------------------------------------------------------------

----------------------------------------------------------------
From: support@laptopsolutions.com
To: john.doe@email.com
Date: Monday, 22 September 2023 12:30 PM
Subject: RE: Urgent Assistance Needed with My Laptop

Hello John,

Thank you for reaching out to us. We're sorry to hear about the issues you're experiencing with your laptop.

For the sudden shutdowns, it sounds like your laptop might be overheating, especially if it's getting hot. We recommend:
1. Ensuring the laptop is on a hard, flat surface for proper ventilation.
2. Regularly cleaning any dust or debris from the vents.
3. Avoiding running too many resource-intensive applications simultaneously.

Regarding the battery issue:
1. Check your screen brightness and lower it if set too high.
2. Turn off any unnecessary background applications.
3. Review your battery health in the system settings to see if it's deteriorating.

If these initial steps don't help, please get back to us, and we'll advise further.

Warm regards,
Laptop Solutions Support Team
----------------------------------------------------------------

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

Thank you for the quick response. I tried the suggestions you provided. The laptop still feels warm, but the shutdowns are less frequent. However, the battery still drains quickly even after reducing the brightness and closing background applications. 

Would it be best to bring it into your store for a professional check?

Regards,
John Doe
----------------------------------------------------------------
----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 24 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

What the hell is happening? i have no reponse yet! are you guys gonna help me or what?
Im getting fedup of your service! its been a day or more, no response.
need an update asap .. please escalate ticket status with available executive at the earliest.

Regards,
John Doe
----------------------------------------------------------------


"""

prompt = f"""

Given the customer email delimited by ```, \
Identify the last statement of the email and set the status to one of the following \
a.Cancelled b.open c.closed,d.Escalate e.check with logistics
Identify if the sentiment is negative \
Identify the topic not more than one.
Identify the problem statement,cause of problem,troubleshooting steps, if troubleshooted or not , status 
Customer Email: ```{mail}```
Json object: Key:(email,status,sentiment,topics,problem statement,cause of problem,troubleshooting steps, if troubleshooted or not)
"""
response = get_completion(prompt, temperature=0.7)
print(response)

mail="""

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 10:14 AM
Subject: Urgent Assistance Needed with My Laptop

Hello Support Team,

I recently purchased a laptop from your store, and I'm encountering a couple of issues that are affecting my ability to use it effectively. 

Firstly, my laptop suddenly shuts down without any warning. I've noticed that it tends to get quite hot around the base, especially when I'm using resource-intensive applications. Secondly, the battery drains incredibly fast. Even with minimal usage, it doesn't last more than 2 hours.

Can you please help?

Thank you,
John Doe
----------------------------------------------------------------

----------------------------------------------------------------
From: support@laptopsolutions.com
To: john.doe@email.com
Date: Monday, 22 September 2023 12:30 PM
Subject: RE: Urgent Assistance Needed with My Laptop

Hello John,

Thank you for reaching out to us. We're sorry to hear about the issues you're experiencing with your laptop.

For the sudden shutdowns, it sounds like your laptop might be overheating, especially if it's getting hot. We recommend:
1. Ensuring the laptop is on a hard, flat surface for proper ventilation.
2. Regularly cleaning any dust or debris from the vents.
3. Avoiding running too many resource-intensive applications simultaneously.

Regarding the battery issue:
1. Check your screen brightness and lower it if set too high.
2. Turn off any unnecessary background applications.
3. Review your battery health in the system settings to see if it's deteriorating.

If these initial steps don't help, please get back to us, and we'll advise further.

Warm regards,
Laptop Solutions Support Team
----------------------------------------------------------------

----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 22 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

Thank you for the quick response. I tried the suggestions you provided. The laptop still feels warm, but the shutdowns are less frequent. However, the battery still drains quickly even after reducing the brightness and closing background applications. 

Would it be best to bring it into your store for a professional check?

Regards,
John Doe
----------------------------------------------------------------
----------------------------------------------------------------
From: john.doe@email.com
To: support@laptopsolutions.com
Date: Monday, 24 September 2023 02:45 PM
Subject: RE: RE: Urgent Assistance Needed with My Laptop

Hello,

Can you help me with the status of the order in transit .
The number to track the logistics is xw000112001.
Havent recieved the goods yet.

Regards,
John Doe
----------------------------------------------------------------


"""

prompt = f"""

Given the customer email delimited by ```, \
evalutate the last statement of the email and set the status to one of the following \
a.Cancelled b.open c.closed,d.Escalate e.check with logistics
Identify if the sentiment is negative \
Identify the topic not more than one.
Identify the problem statement,cause of problem,troubleshooting steps, if troubleshooted or not , status 
Customer Email: ```{mail}```
Json object: Key:(email content,status,sentiment,topics,problem statement,cause of problem,troubleshooting steps, if troubleshooted or not)
"""
response = get_completion(prompt, temperature=0.7)
print(response)






