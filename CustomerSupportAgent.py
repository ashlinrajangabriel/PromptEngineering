import openai
import os

def get_completion(prompt, model="gpt-3.5-turbo",temperature=0): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

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


review = """ Dear support,

I am very upset with the product. my product battery drains instantly in a 1 hr . it heats up like hell. and more importantly the sound stops working after some time.
Please help fix it.

cheers
G
"""

prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review identify and add 1.Problem statement 2. Troubleshooting steps 3. Resolutions and 4.Cause of problem from ```{problems}```.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response = get_completion(prompt, temperature=0.7)
print(response)



"""
Dear G,

Thank you for reaching out and sharing your experience with our product. We sincerely apologize for the inconvenience you have faced.

Based on the details you provided, it seems that you are experiencing multiple issues with your laptop, including quick battery drainage, overheating, and sound problems. These issues can be frustrating, and we understand how important it is to have a fully functional device.

To address these problems, we recommend the following troubleshooting steps:

1. Check the battery health in the system settings to determine if it needs replacement.
2. Clean the cooling vents to ensure proper airflow and prevent overheating.
3. Verify the sound settings and reinstall the sound drivers to resolve the sound issue.

If these troubleshooting steps do not resolve the issues, we recommend contacting our customer service team directly. They have the expertise to provide further assistance and explore additional solutions tailored to your specific situation.

Once again, we apologize for any inconvenience caused and appreciate your patience. We are committed to ensuring your satisfaction and will do our best to resolve these issues promptly.

If you have any further questions or concerns, please do not hesitate to reach out to us.

Best regards,
AI customer agent

"""

