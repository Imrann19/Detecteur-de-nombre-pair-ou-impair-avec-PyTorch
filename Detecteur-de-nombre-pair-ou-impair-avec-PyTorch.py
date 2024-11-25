import torch
import torch.nn as nn

x = torch.tensor([[1], [2], [3], [4], [5], [6], [7], [8], [9]], dtype = torch.float32)
y = torch.tensor([[1], [0], [1], [0], [1], [0], [1], [0], [1]], dtype = torch.float32)

model = nn.Sequential(
    nn.Linear(1, 1),
    nn.Sigmoid()
)

loss_fn = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

for epoch in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

while True:
    try:
        nombre = int(input("Saisissez un nombre (ou taper entrer pour quitter) : "))
    except ValueError:
        print("Programme terminé.")
        break
    test = torch.tensor([[nombre]], dtype = torch.float32)
    resultat = 'impair' if model(test).item() > 0.5 else 'pair'
    print(f"Le nombre {nombre} est {resultat}.\n")