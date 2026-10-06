import numpy as np
from sklearn.linear_model import LinearRegression

# ১. ট্রেনিং ডেটা (যেমন: ইউনিট ব্যবহার -> বিলের পরিমাণ)
# X = ব্যবহৃত ইউনিট (Units), y = মোট বিল (BDT)
X = np.array([[50], [100], [150], [200], [250], [300]])
y = np.array([300, 650, 1000, 1400, 1850, 2300])

# ২. মডেল তৈরি ও ট্রেনিং
model = LinearRegression()
model.fit(X, y)

# ৩. নতুন ইউনিটের জন্য বিল প্রেডিকশন
units_consumed = 180
predicted_bill = model.predict([[units_consumed]])

print(f"স্মার্ট বিল প্রেডিকশন রেজাল্ট:")
print(f"ব্যবহার করা ইউনিট: {units_consumed}")
print(f"আনুমানিক বিল: {predicted_bill[0]:.2f} BDT")