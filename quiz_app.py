import streamlit as st

def main():
    st.title("System Hacking Quiz")
    st.markdown("Test your knowledge of system hacking concepts, password attacks, and authentication protocols.")

    questions = [
        {
            "question": "What are the phases of the System Hacking Methodology?",
            "options": ["A) Gaining Access, Cracking Passwords, Vulnerability Exploitation, Escalating Privileges",
                        "B) Footprinting, Scanning, Enumeration, Reporting",
                        "C) Network Mapping, Social Engineering, Data Exfiltration"],
            "answer": "A) Gaining Access, Cracking Passwords, Vulnerability Exploitation, Escalating Privileges",
            "explanation": "The phases include gaining access, password cracking, exploitation, and privilege escalation."
        },
        {
            "question": "Which of the following is a passive online attack?",
            "options": ["A) Brute-force attack", "B) Packet sniffing", "C) Dictionary attack"],
            "answer": "B) Packet sniffing",
            "explanation": "Passive attacks like packet sniffing do not interact directly with the target."
        },
        {
            "question": "What is the purpose of a rainbow table in offline attacks?",
            "options": ["A) To encrypt passwords",
                        "B) To store pre-computed password hashes for comparison",
                        "C) To generate random passwords"],
            "answer": "B) To store pre-computed password hashes for comparison",
            "explanation": "Rainbow tables speed up password cracking by comparing pre-computed hashes."
        },
        {
            "question": "Which authentication protocol uses a Ticket-Granting Server (TGS)?",
            "options": ["A) NTLM", "B) Kerberos", "C) SAM"],
            "answer": "B) Kerberos",
            "explanation": "Kerberos uses a TGS to issue session tickets for authentication."
        },
        {
            "question": "What does password salting achieve?",
            "options": ["A) Makes passwords easier to reverse-engineer",
                        "B) Adds random characters to passwords to strengthen hashes",
                        "C) Stores passwords in plaintext"],
            "answer": "B) Adds random characters to passwords to strengthen hashes",
            "explanation": "Salting adds randomness to hashes, making them harder to crack."
        },
        {
            "question": "Which tool is used for password cracking on Windows systems?",
            "options": ["A) Wireshark", "B) Cain and Abel", "C) Nmap"],
            "answer": "B) Cain and Abel",
            "explanation": "Cain and Abel is a popular Windows password-cracking tool."
        },
        {
            "question": "True or False: Default passwords are a secure way to protect systems.",
            "options": ["True", "False"],
            "answer": "False",
            "explanation": "Default passwords are often publicly known and insecure."
        },
        {
            "question": "What countermeasure prevents password hash reversal?",
            "options": ["A) Multi-factor authentication", "B) Password salting", "C) Using shorter passwords"],
            "answer": "B) Password salting",
            "explanation": "Salting makes hashes harder to reverse-engineer."
        },
        {
            "question": "Which attack involves capturing and replaying network packets?",
            "options": ["A) Brute-force", "B) Replay attack", "C) Dictionary attack"],
            "answer": "B) Replay attack",
            "explanation": "Replay attacks resend captured packets to gain access."
        },
        {
            "question": "What is stored in the SAM database?",
            "options": ["A) Plaintext passwords", "B) User account hashes", "C) Encryption keys"],
            "answer": "B) User account hashes",
            "explanation": "The SAM database stores hashed credentials."
        }
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        
        # Use radio for single-select questions
        selected_option = st.radio("Choose an answer:", q["options"], key=f"q{i}", index=None)

        if st.button("Check Answer", key=f"btn{i}"):
            if selected_option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            
            with st.expander("Explanation"):
                st.write(q["explanation"])
            
            st.write("---")

    st.header("Quiz Results")
    st.write(f"Your score: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()