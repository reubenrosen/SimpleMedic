
# SimpleMedic- An NLP based approach to identifying conditions based on symptoms

This python GUI utilizes tkinter and Natural Language Processing, specifically lemmetization to identify words, associate them to the list of conditions listed in symptoms_dataset.csv (a small dataset I made for testing purposes)




## Deployment

Install packages via

```bash
  pip install -r requirements. txt
```
Make sure you have the symptom_model folder in the same directory as simple_medic.py. The file is large so I uploaded it here:

https://drive.google.com/file/d/1rJiXcJqHhgn_U7A_eyL4RuX9zHuyHh_d/view?usp=sharing

The above zip file contains symptoms_model, which can be extracted into the same directory as the main python script.

and then to run the GUI you can run
```bash
  python simple_medic.py
```

Alternatively I compiled a Windows executable which can be run. However it still relies on symptom_model folder, so I compressed it into a zip file as below:

https://drive.google.com/file/d/1CBiMQG1vdpp-vaFZKYO_T3qT1RlCGRHH/view?usp=sharing




## Screenshots

![Screenshot](https://github.com/reubenrosen/SimpleMedic/blob/main/images/image1.png)

![Screenshot](https://github.com/reubenrosen/SimpleMedic/blob/main/images/image2.png)

