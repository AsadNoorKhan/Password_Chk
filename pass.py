import streamlit as st

def checker(password):
    strength = {"strong": [5], "moderate": [3, 4], "weak": [1, 2]}
    sp = "!@#$%^&*"
    min_len = 8
    score = 0
    flag = {"length": False, "number": False, "special_character": False, "upper_case": False, "lower_case": False}

    if len(password) >= min_len:
        score += 1
        flag["length"] = True

    if any(i in sp for i in password):
        score += 1
        flag["special_character"] = True

    for i in password:
        if i.isdigit():
            flag["number"] = True
        if i.isupper():
            flag["upper_case"] = True
        if i.islower():
            flag["lower_case"] = True

    score += sum(flag[key] for key in ["number", "upper_case", "lower_case"])
    false_flags = [key for key, value in flag.items() if not value]

    return score, false_flags

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

st.markdown("<h2 style='text-align: center;'>🔐 Password Strength Checker</h2>", unsafe_allow_html=True)

st.write("### Password Rules")
st.markdown("""
- ✅ **At least 8 characters long**
- ✅ **Uppercase & lowercase letters**
- ✅ **At least one digit (0-9)**
- ✅ **At least one special character (!@#$%^&*)**
""")

# Password input
password_input = st.text_input("🔑 Enter your password", type="password")

# Check strength
score, false_flags = checker(password_input)

# Color + Label based on score
if score == 5:
    color = "#22C55E"
    label = "💪 Strong"
elif score >= 3:
    color = "#FACC15"
    label = "⚠️ Moderate"
elif score >= 1:
    color = "#FF4B4B"
    label = "❌ Weak"
else:
    color = "#ddd"
    label = "Very Weak"

# Progress Bar style (no double track)
st.write("### Password Strength")

st.markdown(f"""
<div style="background-color: #ddd; border-radius: 0.75rem; height: 20px; overflow: hidden;">
  <div style="
    width: {(score/5)*100}%;
    background-color: {color};
    height: 100%;
    transition: width 0.3s ease;
  "></div>
</div>
<p style='text-align:center; margin-top: 5px; font-size: 18px;'>{label}</p>
""", unsafe_allow_html=True)

# Feedback message and suggestions
if password_input:
    if score == 5:
        st.success("✅ Strong Password!")
    elif score >= 3:
        st.warning(f"⚠️ Moderate Password – Consider adding: {', '.join(false_flags)}")
    elif score >= 1:
        st.error(f"❌ Weak Password – Improve it by adding: {', '.join(false_flags)}")
    else:
        st.error(f"❌ Very Weak – Consider adding: {', '.join(false_flags)}")

    if false_flags:
        st.write("### Suggestions to improve your password:")
        for missing in false_flags:
            st.write(f"- ➕ Add {missing.replace('_', ' ')}")
else:
    st.info("Please enter a password to check.")

st.markdown("<hr style='margin-top:30px;'/><p style='text-align:center;font-size:12px;'>🔒 Stay secure with strong, unique passwords!</p>", unsafe_allow_html=True)
