import ttkbootstrap as tb
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the fine-tuned model and tokenizer
model = BertForSequenceClassification.from_pretrained("./symptom_model")
tokenizer = BertTokenizer.from_pretrained("./symptom_model")
model.eval()  # Put model in evaluation mode

# Class labels (make sure they match your training labels)
classes = ['Flu', 'Common Cold', 'COVID-19', 'Migraine', 'Food Poisoning',
           'Allergies', 'Asthma Attack', 'Stomach Ulcer', 'Anxiety Attack', 'Pneumonia']

# Create the Tkinter window
app = tb.Window(themename="flatly")
app.title("SimpleMedic")
app.geometry("500x400")  # Adjusted window size

# Label for introduction
intro_label = tb.Label(app, text="SimpleMedic: Enter your symptoms below", font=("Arial", 18, 'bold'))
intro_label.pack(pady=15)

# Entry widget for user input (symptoms)
entry = tb.Entry(app, width=45, font=("Arial", 12), bootstyle="dark", justify="center")
entry.pack(pady=15)

# Function to predict conditions with probabilities
def predict_condition():
    user_input = entry.get()
    if not user_input.strip():  # If input is empty
        result_label.config(text="❗ Please enter symptoms.")
        return

    # Tokenize the user input
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=64)

    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = torch.softmax(outputs.logits, dim=1)[0]

    # Get top 3 predictions (conditions)
    top_probs, top_indices = torch.topk(probabilities, k=3)
    results = []
    for i in range(3):
        condition = classes[top_indices[i]]
        prob = top_probs[i].item() * 100  # Convert to percentage
        results.append(f"{condition} - {prob:.2f}%")

    # Display the results
    result_text = "\n".join(results)
    result_label.config(text=f"✅ Possible Conditions:\n\n{result_text}")

# Button to trigger the prediction
predict_button = tb.Button(app, text="Analyze Symptoms", bootstyle="primary", command=predict_condition, width=20)
predict_button.pack(pady=10)

# Label to display the predicted conditions and probabilities
result_label = tb.Label(app, text="", font=("Arial", 12), justify="left", wraplength=400)
result_label.pack(pady=20)

# Start the Tkinter event loop
app.mainloop()
