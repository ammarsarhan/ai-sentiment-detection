import tensorflow as tf

# Check TensorFlow installation
print(f"TensorFlow version: {tf.__version__}")

# Create a simple computation graph
a = tf.constant(5)
b = tf.constant(3)
c = a + b

print(f"Result: {c.numpy()}") 