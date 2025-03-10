import streamlit as st
import time
from datetime import datetime
import numpy as np
import base64
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="A MESSAGE FOR YOU SHREYA ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Function to add background image
def add_bg_image(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            img_data = f.read()
            b64_encoded = base64.b64encode(img_data).decode()
            
            # Apply a soft overlay to make text more readable
            bg_style = f"""
            <style>
            .stApp {{
                background-image: url(data:image/jpeg;base64,{b64_encoded});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            .stApp::before {{
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.7);
                z-index: -1;
            }}
            </style>
            """
            st.markdown(bg_style, unsafe_allow_html=True)
    else:
        # Fallback gradient if image doesn't exist
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #fcf2f2 100%);
        }
        </style>
        """, unsafe_allow_html=True)

# Custom CSS with enhanced animations and fonts
def add_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500;700&family=Montserrat:wght@300;400;500&family=Great+Vibes&family=Parisienne&display=swap');
        
 h1 { 
  font-family: 'Pacifico', cursive !important;  
  color: white;  
  font-size: 3.2rem !important;  
  text-transform: capitalize; /* Ensures "A" is capitalized in words */
  letter-spacing: 1px;  
  text-shadow: 2px 2px 5px rgba(255, 182, 193, 0.8); /* Soft pink glow */
}


        
        h2, h3 {
            font-family: 'Parisienne', cursive !important;
            color: #d23b68;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.05);
        }
        
        /* Changed font for "Listen to My Voice" */
        h2:contains("Listen to My Voice") {
            font-family: 'Montserrat', sans-serif !important;
            color: white !important;
        }
        
        .letter-text {
            font-family: 'Dancing Script', cursive;
            font-size: 1.5rem;
            font-weight: 500;
            line-height: 1.8;
            color: #d23b68;
            padding: 25px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.85);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.5);
        }
        
        .letter-container {
            padding: 25px;
            border-radius: 20px;
            background: linear-gradient(45deg, #ffefef 0%, #fff1f7 100%);
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
            margin: 30px 0;
            position: relative;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: letterAppear 1s ease forwards;
        }
        
        @keyframes letterAppear {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        
        .letter-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        
        .letter-container::before {
            content: '';
            position: absolute;
            top: -15px;
            right: -15px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, transparent 50%, #d67a95 50%);
            transform: rotate(45deg);
            z-index: 1;
            box-shadow: -2px 2px 5px rgba(0,0,0,0.1);
        }
        
        .stButton button {
            background: linear-gradient(45deg, #ff5b84, #ff8fb1);
            color: white;
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
            font-size: 1.1rem;
            letter-spacing: 0.5px;
            border-radius: 30px;
            padding: 12px 35px;
            border: none;
            box-shadow: 0 8px 20px rgba(255, 91, 132, 0.4);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: pulse 2s infinite;
        }
        
        .stButton button:hover {
            background: linear-gradient(45deg, #d23b68, #ff5b84);
            box-shadow: 0 10px 25px rgba(210, 59, 104, 0.5);
            transform: translateY(-3px) scale(1.05);
            animation: none;
        }
        
        .audio-section {
            margin-top: 40px;
            padding: 25px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.75);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            animation: fadeIn 1s ease 1.5s forwards;
            opacity: 0;
            transform: translateY(20px);
        }
        
        .audio-section h2 {
            font-family: 'Montserrat', sans-serif !important;
            color: white !important;
        }
        
        @keyframes fadeIn {
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Floating hearts animation */
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) rotate(720deg); opacity: 0; }
        }
        
        .floating-heart {
            position: fixed;
            z-index: -1;
            animation: float linear infinite;
            filter: drop-shadow(0 3px 5px rgba(0, 0, 0, 0.1));
        }
        
        /* Envelope animation */
        .envelope {
            text-align: center;
            margin: 40px 0;
            animation: bounceIn 1.2s cubic-bezier(0.68, -0.55, 0.27, 1.55);
        }
        
        @keyframes bounceIn {
            0% { transform: scale(0); opacity: 0; }
            60% { transform: scale(1.2); }
            80% { transform: scale(0.9); }
            100% { transform: scale(1); opacity: 1; }
        }
        
        .envelope-icon {
            font-size: 120px;
            background: linear-gradient(45deg, #ff5b84, #ff8fb1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 3px 5px rgba(0, 0, 0, 0.2));
            animation: pulse 2s infinite, wiggle 6s ease-in-out infinite;
            display: inline-block;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        @keyframes wiggle {
            0%, 100% { transform: rotate(-3deg); }
            50% { transform: rotate(3deg); }
        }
        
        /* Heart beat animation */
        .heart-icon {
            font-size: 100px;
            background: linear-gradient(45deg, #ff5b84, #ff8fb1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 3px 5px rgba(0, 0, 0, 0.2));
            animation: heartBeat 1.5s infinite, float-subtle 3s ease-in-out infinite;
            display: inline-block;
        }
        
        @keyframes heartBeat {
            0% { transform: scale(1); }
            14% { transform: scale(1.3); }
            28% { transform: scale(1); }
            42% { transform: scale(1.3); }
            70% { transform: scale(1); }
        }
        
        @keyframes float-subtle {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        /* Date display */
        .date-display {
            font-family: 'Montserrat', sans-serif;
            color: #888;
            text-align: right;
            font-style: italic;
            margin-bottom: 20px;
            animation: fadeIn 1s ease;
        }
        
        /* Message text animation */
        @keyframes typeIn {
            from { width: 0; }
            to { width: 100%; }
        }
        
        /* Confetti animation enhanced */
        @keyframes confettiFall {
            0% { transform: translateY(-10px) rotate(0); opacity: 1; }
            100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 40px;
            font-family: 'Montserrat', sans-serif;
            color: #888;
            padding: 15px;
            animation: fadeIn 1s ease 2s forwards;
            opacity: 0;
        }
        
        .footer p {
            position: relative;
            display: inline-block;
        }
        
        .footer p:before, .footer p:after {
            content: "❤️";
            position: absolute;
            top: 0;
            opacity: 0.7;
        }
        
        .footer p:before {
            left: -25px;
        }
        
        .footer p:after {
            right: -25px;
        }
        
        /* Button text animation */
        .button-text {
            position: relative;
            overflow: hidden;
        }
        
        .button-text:after {
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: -100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shimmer 2s infinite;
        }
        
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        /* Info alert styling */
        .stAlert {
            background-color: rgba(255, 255, 255, 0.8) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.5) !important;
            backdrop-filter: blur(5px) !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Function to add floating hearts background (enhanced)
def create_floating_hearts():
    hearts = ""
    heart_types = ["❤️", "💖", "💗", "💕", "💓", "💘"] 
    
    for i in range(30):  # Increased number of hearts
        # Randomize heart properties
        heart_type = np.random.choice(heart_types)
        size = np.random.randint(15, 60)  # Increased size range
        left = np.random.randint(0, 100)
        delay = np.random.randint(0, 15)
        duration = np.random.randint(15, 40)  # Longer durations
        opacity = np.random.uniform(0.3, 0.9)
        
        # More color options
        color = np.random.choice(['#ff5b84', '#ff8fb1', '#ffb6c1', '#ffc8d6', '#d23b68', '#ff4d6d', '#ff7096', '#ff9bba'])
        
        heart = f"""
        <div class="floating-heart" style="
            left: {left}vw;
            font-size: {size}px;
            color: {color};
            opacity: {opacity};
            animation-delay: {delay}s;
            animation-duration: {duration}s;
        ">{heart_type}</div>
        """
        hearts += heart
    
    st.markdown(hearts, unsafe_allow_html=True)

# Initialize session state for one-time reveal
if 'revealed' not in st.session_state:
    st.session_state.revealed = False
if 'show_confetti' not in st.session_state:
    st.session_state.show_confetti = False

# Set background image - replace 'background.jpg' with your image path
add_bg_image("background.jpg")  # You need to place your image file in the same directory

# Add CSS and background hearts
add_custom_css()
create_floating_hearts()

# Your love letter text
love_letter = """
Dear Girlfriend,

Manyyy manyyy happpyyy returns of the dayyyy Shreyaaaa!!!!!.
Its my girlfriend's birthday yeyeeye!!

Its been a year Shreya today, and this year feels so important lucky and happy to me. 
I am so lucky to have you in my life.
Here I am always with you come what may. 
I dont wanna make this a big emo letter :)
May this year bring you as much happiness and love as you bring into my life.

Happy Birthday, my love! 💖
Happy 1 year
Many moreee to come!

Forever yours,
Siddharth
"""

# Main app
st.title(" A Message For You Shreya💌")

# Display date with enhanced styling
#current_date = datetime.now().strftime("%B %d, %Y")
#st.markdown(f"<div class='date-display'>{current_date}</div>", unsafe_allow_html=True)

# Display envelope animation with enhanced effect
if not st.session_state.revealed:
    st.markdown("""
    <div class="envelope">
        <div class="envelope-icon">💌</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; font-family: Parisienne, cursive; color: #d23b68; font-size: 24px; margin-top: -10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.05);'>I've written something special just for you...</p>", unsafe_allow_html=True)
    
    # Enhanced button for opening the letter
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Open Your Letter ✨"):
            st.session_state.revealed = True
            st.session_state.show_confetti = True
            st.rerun()

# If the letter has been revealed
if st.session_state.revealed:
    # Enhanced confetti animation with more particles and colors
    if st.session_state.show_confetti:
        confetti_js = """
        <script>
            function createConfetti() {
                const confettiCount = 300;  // More confetti
                const confettiColors = ['#ff5b84', '#ffb6c1', '#ffc8d6', '#ff8fb1', '#d23b68', '#ff4d6d', '#ff7096', '#ff9bba'];
                const confettiShapes = ['circle', 'square', 'heart'];
                
                const confettiContainer = document.createElement('div');
                confettiContainer.style.position = 'fixed';
                confettiContainer.style.top = '0';
                confettiContainer.style.left = '0';
                confettiContainer.style.width = '100%';
                confettiContainer.style.height = '100%';
                confettiContainer.style.pointerEvents = 'none';
                confettiContainer.style.zIndex = '1000';
                document.body.appendChild(confettiContainer);
                
                for (let i = 0; i < confettiCount; i++) {
                    const confetti = document.createElement('div');
                    const size = Math.random() * 15 + 5;  // Larger confetti
                    const shape = confettiShapes[Math.floor(Math.random() * confettiShapes.length)];
                    
                    confetti.style.position = 'absolute';
                    confetti.style.width = `${size}px`;
                    confetti.style.height = shape === 'heart' ? `${size * 0.8}px` : `${size}px`;
                    confetti.style.backgroundColor = confettiColors[Math.floor(Math.random() * confettiColors.length)];
                    
                    if (shape === 'circle') {
                        confetti.style.borderRadius = '50%';
                    } else if (shape === 'heart') {
                        confetti.style.backgroundColor = 'transparent';
                        confetti.style.boxShadow = 'none';
                        confetti.innerHTML = '❤️';
                        confetti.style.fontSize = `${size}px`;
                        confetti.style.color = confettiColors[Math.floor(Math.random() * confettiColors.length)];
                    }
                    
                    confetti.style.top = '-20px';
                    confetti.style.left = `${Math.random() * 100}vw`;
                    confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
                    
                    const duration = Math.random() * 4 + 3;  // Longer duration
                    const delay = Math.random() * 3;
                    
                    confetti.style.animation = `confettiFall ${duration}s ease-in ${delay}s forwards`;
                    
                    confettiContainer.appendChild(confetti);
                }
                
                const style = document.createElement('style');
                style.innerHTML = `
                    @keyframes confettiFall {
                        0% { transform: translateY(-20px) rotate(0); opacity: 1; }
                        25% { transform: translateY(25vh) translateX(${Math.random() > 0.5 ? '+' : '-'}25px) rotate(45deg); }
                        50% { transform: translateY(50vh) translateX(${Math.random() > 0.5 ? '-' : '+'}25px) rotate(90deg); }
                        75% { transform: translateY(75vh) translateX(${Math.random() > 0.5 ? '+' : '-'}25px) rotate(180deg); }
                        100% { transform: translateY(100vh) translateX(${Math.random() > 0.5 ? '-' : '+'}50px) rotate(360deg); opacity: 0; }
                    }
                `;
                document.head.appendChild(style);
                
                setTimeout(() => {
                    confettiContainer.remove();
                    style.remove();
                }, 7000);  // Longer display time
            }
            
            // Run once when page loads
            createConfetti();
        </script>
        """
        st.markdown(confetti_js, unsafe_allow_html=True)
        st.session_state.show_confetti = False  # Only show once
    
    # Display the heart animation with enhanced effect
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <div class="heart-icon">❤️</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the letter with enhanced animation
    st.markdown("<div class='letter-container'>", unsafe_allow_html=True)
    
    # Create a placeholder for the animated text
    letter_placeholder = st.empty()
    
    # Enhanced animation effect (only runs once per session)
    lines = love_letter.strip().split('\n')
    full_text = ""
    
    for line in lines:
        if line.strip() == "":
            full_text += "<br><br>"
            letter_placeholder.markdown(f"<div class='letter-text'>{full_text}</div>", unsafe_allow_html=True)
            time.sleep(0.4)  # Slightly longer pauses between paragraphs
        else:
            words = line.split(" ")
            for word in words:
                full_text += word + " "
                letter_placeholder.markdown(f"<div class='letter-text'>{full_text}</div>", unsafe_allow_html=True)
                time.sleep(0.12)  # Slightly faster typing for better flow
            full_text += "<br>"
            letter_placeholder.markdown(f"<div class='letter-text'>{full_text}</div>", unsafe_allow_html=True)
            time.sleep(0.2)  # Pause at end of line
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add enhanced audio message section
    st.markdown("<div class='audio-section'>", unsafe_allow_html=True)
    st.markdown("## 🎙️ Listen to My Voice")
    st.markdown("<p style='font-family: Montserrat; font-size: 18px; color: #d23b68;'>I recorded this special message just for you ❤️</p>", unsafe_allow_html=True)
    
    # Handling the audio file with error checking
    try:
        st.audio("voice_message.mp3", format="audio/mp3")
    except:
        st.warning("Voice message waiting to be added. To complete your gift, record a special message and save it as 'voice_message.mp3'")
        st.markdown("""
        <div style="font-family: Montserrat; color: #888; font-size: 14px; margin-top: 15px;">
            <p>To add your voice message:</p>
            <ol>
                <li>Record a special birthday message using your phone or computer</li>
                <li>Save it as MP3 format</li>
                <li>Name it "voice_message.mp3" and place it in the same folder as this app</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add an enhanced footer
    st.markdown("""
    <div class='footer'>
        <p>Made with love, just for you</p>
    </div>
    """, unsafe_allow_html=True)
