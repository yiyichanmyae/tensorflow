import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

cross_entropy = -tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

# Print cross entropy from session
with tf.Session() as session:
    output = session.run(cross_entropy, feed_dict={ one_hot:one_hot_data, softmax:softmax_data })
    
print(output)