import streamlit as st
import cv2
import mediapipe as mp
import time
import random

class Question:
    def __init__(self,ques,options,ans):
        self.ques=ques
        self.options=options
        self.ans=ans

q1 = Question("What is the capital of India?", {"A": "Mumbai", "B": "Delhi", "C": "Kolkata", "D": "Chennai"}, "B")
q2 = Question("Who was the first Prime Minister of India?", {"A": "Indira Gandhi", "B": "Rajiv Gandhi", "C": "Jawaharlal Nehru", "D": "Lal Bahadur Shastri"}, "C")
q3 = Question("Which is the largest state in India by area?", {"A": "Uttar Pradesh", "B": "Madhya Pradesh", "C": "Maharashtra", "D": "Rajasthan"}, "D")
q4 = Question("Which is the national bird of India?", {"A": "Peacock", "B": "Sparrow", "C": "Eagle", "D": "Parrot"}, "A")
q5 = Question("Where is the Taj Mahal located?", {"A": "Delhi", "B": "Agra", "C": "Mumbai", "D": "Jaipur"}, "B")
q6 = Question("Who wrote the Indian national anthem?", {"A": "Rabindranath Tagore", "B": "Bankim Chandra Chattopadhyay", "C": "Mahatma Gandhi", "D": "Jawaharlal Nehru"}, "A")
q7 = Question("Which river is the longest in India?", {"A": "Godavari", "B": "Kaveri", "C": "Ganga", "D": "Yamuna"}, "C")
q8 = Question("Who is known as the 'Father of the Nation' in India?", {"A": "Mahatma Gandhi", "B": "Jawaharlal Nehru", "C": "Subhas Chandra Bose", "D": "B. R. Ambedkar"}, "A")
q9 = Question("Which is the highest peak in India?", {"A": "Kanchenjunga", "B": "Nanda Devi", "C": "Kamet", "D": "K2"}, "D")
q10 = Question("Which is the largest freshwater lake in India?", {"A": "Dal Lake", "B": "Wular Lake", "C": "Pulicat Lake", "D": "Vembanad Lake"}, "B")
q11 = Question("Who was the first woman Prime Minister of India?", {"A": "Indira Gandhi", "B": "Pratibha Patil", "C": "Sonia Gandhi", "D": "Sarojini Naidu"}, "A")
q12 = Question("Which city is known as the 'Silicon Valley of India'?", {"A": "Hyderabad", "B": "Mumbai", "C": "Bengaluru", "D": "Chennai"}, "C")
q13 = Question("What is the national animal of India?", {"A": "Lion", "B": "Elephant", "C": "Tiger", "D": "Peacock"}, "C")
q14 = Question("Who is the author of the book 'Discovery of India'?", {"A": "Rabindranath Tagore", "B": "Mahatma Gandhi", "C": "Jawaharlal Nehru", "D": "Subhas Chandra Bose"}, "C")
q15 = Question("Which Indian state is the largest producer of tea?", {"A": "Kerala", "B": "Tamil Nadu", "C": "West Bengal", "D": "Assam"}, "D")
q16 = Question("Who was the first President of India?", {"A": "Rajendra Prasad", "B": "Sarvepalli Radhakrishnan", "C": "Zakir Husain", "D": "V. V. Giri"}, "A")
q17 = Question("Which is the smallest state in India by area?", {"A": "Sikkim", "B": "Goa", "C": "Tripura", "D": "Meghalaya"}, "B")
q18 = Question("Which Indian city is known as the 'City of Joy'?", {"A": "Mumbai", "B": "Delhi", "C": "Kolkata", "D": "Chennai"}, "C")
q19 = Question("Who was the first Indian to win the Nobel Prize?", {"A": "Har Gobind Khorana", "B": "C. V. Raman", "C": "Rabindranath Tagore", "D": "Subrahmanyan Chandrasekhar"}, "C")
q20 = Question("Which Indian state has the longest coastline?", {"A": "Kerala", "B": "Tamil Nadu", "C": "Gujarat", "D": "Andhra Pradesh"}, "C")
q21 = Question("Which Indian city is known as the 'Pink City'?", {"A": "Jaipur", "B": "Delhi", "C": "Agra", "D": "Lucknow"}, "A")
q22 = Question("Who was the first Indian woman in space?", {"A": "Kalpana Chawla", "B": "Sunita Williams", "C": "Indira Gandhi", "D": "Pratibha Patil"}, "A")
q23 = Question("Which is the largest river island in India?", {"A": "Majuli", "B": "Srirangam", "C": "Bhavani Island", "D": "Diu Island"}, "A")
q24 = Question("Who is known as the 'Missile Man of India'?", {"A": "Vikram Sarabhai", "B": "Homi J. Bhabha", "C": "Satish Dhawan", "D": "A.P.J. Abdul Kalam"}, "D")
q25 = Question("Which Indian state is known as the 'Land of Five Rivers'?", {"A": "Gujarat", "B": "Punjab", "C": "Haryana", "D": "Uttar Pradesh"}, "B")
q26 = Question("Who was the first Indian to win an individual Olympic gold medal?", {"A": "Abhinav Bindra", "B": "Rajyavardhan Singh Rathore", "C": "Vijender Singh", "D": "Sushil Kumar"}, "A")
q27 = Question("Which is the largest desert in India?", {"A": "Thar Desert", "B": "Kutch Desert", "C": "Ladakh Desert", "D": "Deccan Desert"}, "A")
q28 = Question("Who is the author of the epic 'Mahabharata'?", {"A": "Valmiki", "B": "Ved Vyas", "C": "Tulsidas", "D": "Kabir"}, "B")
q29 = Question("Which is the largest lake in India?", {"A": "Dal Lake", "B": "Chilika Lake", "C": "Pulicat Lake", "D": "Wular Lake"}, "D")
q30 = Question("Who built the Qutub Minar?", {"A": "Qutb-ud-din Aibak", "B": "Akbar", "C": "Shah Jahan", "D": "Aurangzeb"}, "A")
q31 = Question("Which Indian city is known as the 'City of Lakes'?", {"A": "Udaipur", "B": "Bhopal", "C": "Lucknow", "D": "Hyderabad"}, "A")
q32 = Question("Who was the first Indian to win the Booker Prize?", {"A": "Arundhati Roy", "B": "Salman Rushdie", "C": "Kiran Desai", "D": "V. S. Naipaul"}, "A")
q33 = Question("Which is the largest museum in India?", {"A": "National Museum, Delhi", "B": "Indian Museum, Kolkata", "C": "Salar Jung Museum, Hyderabad", "D": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya, Mumbai"}, "B")
q34 = Question("Who is known as the 'Nightingale of India'?", {"A": "Lata Mangeshkar", "B": "Sarojini Naidu", "C": "Indira Gandhi", "D": "Mother Teresa"}, "B")
q35 = Question("Which is the largest planetarium in India?", {"A": "Nehru Planetarium, Delhi", "B": "Birla Planetarium, Kolkata", "C": "Anna Science Centre Planetarium, Tiruchirappalli", "D": "Gujarat Science City, Ahmedabad"}, "B")
q36 = Question("Who was the first Indian to go into space?", {"A": "Kalpana Chawla", "B": "Rakesh Sharma", "C": "Sunita Williams", "D": "A.P.J. Abdul Kalam"}, "B")
q37 = Question("Which is the largest zoo in India?", {"A": "Arignar Anna Zoological Park, Chennai", "B": "Nandankanan Zoological Park, Bhubaneswar", "C": "National Zoological Park, Delhi", "D": "Alipore Zoological Gardens, Kolkata"}, "A")
q38 = Question("Who is the author of the novel 'The God of Small Things'?", {"A": "Arundhati Roy", "B": "Salman Rushdie", "C": "Vikram Seth", "D": "Amitav Ghosh"}, "A")
q39 = Question("Which is the highest waterfall in India?", {"A": "Jog Falls, Karnataka", "B": "Nohkalikai Falls, Meghalaya", "C": "Dudhsagar Falls, Goa", "D": "Kunchikal Falls, Karnataka"}, "D")
q40 = Question("Which sea is located to the west of India?", {"A": "Arabian Sea", "B": "Bay of Bengal", "C": "Indian Ocean", "D": "Red Sea"}, "A")
q41 = Question("Which Indian city is known as the 'City of Pearls'?", {"A": "Jaipur", "B": "Hyderabad", "C": "Kolkata", "D": "Mumbai"}, "B")
q42 = Question("Who was the first Indian woman to climb Mount Everest?", {"A": "Bachendri Pal", "B": "Santosh Yadav", "C": "Arunima Sinha", "D": "Malavath Purna"}, "A")
q43 = Question("Which is the largest cave temple in India?", {"A": "Ellora Caves, Maharashtra", "B": "Ajanta Caves, Maharashtra", "C": "Elephanta Caves, Maharashtra", "D": "Badami Cave Temples, Karnataka"}, "A")
q44 = Question("Who is known as the 'Iron Man of India'?", {"A": "Subhas Chandra Bose", "B": "B. R. Ambedkar", "C": "Sardar Vallabhbhai Patel", "D": "Jawaharlal Nehru"}, "C")
q45 = Question("Which is the largest river island in the world?", {"A": "Majuli, Assam", "B": "Umananda, Assam", "C": "Srirangam, Tamil Nadu", "D": "Bhavani Island, Andhra Pradesh"}, "A")
q46 = Question("Who was the first Indian to win a medal in the Olympics?", {"A": "Khashaba Dadasaheb Jadhav", "B": "Leander Paes", "C": "Rajyavardhan Singh Rathore", "D": "Norman Pritchard"}, "D")
q47 = Question("Which is the largest fort in India?", {"A": "Red Fort, Delhi", "B": "Agra Fort, Uttar Pradesh", "C": "Gwalior Fort, Madhya Pradesh", "D": "Chittorgarh Fort, Rajasthan"}, "D")
q48 = Question("Who is the author of the novel 'Midnight's Children'?", {"A": "Salman Rushdie", "B": "Vikram Seth", "C": "Arundhati Roy", "D": "Amitav Ghosh"}, "A")
q49 = Question("Which is the largest saltwater lake in India?", {"A": "Chilika Lake, Odisha", "B": "Pulicat Lake, Andhra Pradesh", "C": "Sambhar Lake, Rajasthan", "D": "Wular Lake, Jammu and Kashmir"}, "A")
q50 = Question("Who is the current Prime Minister of India?", {"A": "Narendra Modi", "B": "Manmohan Singh", "C": "Atal Bihari Vajpayee", "D": "Rajiv Gandhi"}, "A")
Questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50]

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Initialize MediaPipe Drawing Utility
mp_drawing = mp.solutions.drawing_utils

st.title('Quiz Application')
st.subheader("Take this quiz and test your knowledge about India")


def get():

    selected_ans=None
    
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    # Variables to track the quadrant and time
    last_quadrant = None
    start_time = None
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Flip the image horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape

        # Draw lines to divide the frame into 4 quadrants
        cv2.line(frame, (width//2, 0), (width//2, height), (255, 0, 0), 2)
        cv2.line(frame, (0, height//2), (width, height//2), (255, 0, 0), 2)

        # Convert the BGR image to RGB before processing
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Draw the hand annotations on the image
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the coordinates of the center of the hand
                cx, cy = int(hand_landmarks.landmark[0].x * width), int(hand_landmarks.landmark[0].y * height)

                # Determine the quadrant
                quadrant = 'A' if cx < width//2 and cy < height//2 else \
                           'B' if cx > width//2 and cy < height//2 else \
                           'C' if cx < width//2 and cy > height//2 else 'D'

                # Check if the hand is in the same quadrant
                if quadrant == last_quadrant:
                    # If the hand has been in the quadrant for more than 3 seconds
                    if time.time() - start_time > 3:
                        selected_ans=quadrant
                        start_time = time.time()

                        # Close the camera and windows
                        cap.release()
                        cv2.destroyAllWindows()

                       
                else:
                    # Update the last quadrant and start time
                    last_quadrant = quadrant
                    start_time = time.time()

                # Display the quadrant on the frame
                cv2.putText(frame, quadrant, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Close the camera and windows
    cap.release()
    cv2.destroyAllWindows()

    return quadrant



def play():

    ques_no=1
    scores=[]
    total_score=0
    
    selected_questions = random.sample(Questions, 10)
    
    
    placeholder = st.empty()
    response_placeholder=st.empty()
    col1,col2=st.columns(2)


    for current_question in selected_questions:
        # Concatenate question and options into a single string
        content = str(ques_no)+". "+current_question.ques
        for key, value in current_question.options.items():
            content += "\n{}: {}\n".format(key, value)        
        # Write the content to the placeholder
        placeholder.subheader(content)
        time.sleep(3)

        sel=get()
        response="Option {} selected. ".format(sel)
        
        if sel==current_question.ans:
            response+="Correct Answer"
            response_placeholder.write(response)
            total_score=total_score+1
            scores.append([ques_no, "Correct"])
        else:
            response+="Wrong Answer. Correct Answer was {}".format(current_question.ans)
            response_placeholder.write(response)
            scores.append([ques_no, "Wrong"])
        
        time.sleep(1.5)
        ques_no=ques_no+1
        
        # Clear the placeholder
        placeholder.empty()
        response_placeholder.empty()
        time.sleep(1)
    
    st.subheader(name+", Your score is {}/10".format(str(total_score)))
    col1,col2=st.columns(2)
    with col1:
        for item in scores[:5]:
            st.write("Question {} - {}".format(str(item[0]), item[1]))
    with col2:
        for item in scores[5:]:
            st.write("Question {} - {}".format(str(item[0]), item[1]))
    
    # Add a restart button
    if st.button("Play again"):
        # Clear everything
        st.experimental_rerun()
    
    
# Create a placeholder for the name input field
name_placeholder = st.empty()

# Create a placeholder for the play button
button_placeholder = st.empty()

# Get the user's name
name = name_placeholder.text_input("Please enter your name:")

# Display the play button
play_button = button_placeholder.button("Play")

# If the play button is clicked and a name is entered, start the game
if play_button and name:
    # Clear the name input field and the play button
    name_placeholder.empty()
    button_placeholder.empty()

    # Call the play function
    play()
