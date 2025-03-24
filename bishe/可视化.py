import json
import matplotlib.pyplot as plt

# 读取训练日志
log_path = "/Users/wenzengpei/Downloads/CycleGAN Classifier Results/log.json"

with open(log_path, 'r') as f:
    logs = json.load(f)

# 提取数据
epochs = [log["epoch"] for log in logs]
train_loss = [log["train/loss"] for log in logs]
valid_acc = [log["valid/accuracy"] for log in logs]

# 创建图像
plt.figure(figsize=(10, 5))

# 训练损失曲线
plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, label="Train Loss", color="blue")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss Curve")
plt.legend()

# 验证准确率曲线
plt.subplot(1, 2, 2)
plt.plot(epochs, valid_acc, label="Validation Accuracy", color="red")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Validation Accuracy Curve")
plt.legend()

plt.show()
