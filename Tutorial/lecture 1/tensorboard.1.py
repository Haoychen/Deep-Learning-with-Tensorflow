import tensorflow as tf
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as sess:
    # To activate TensorBoard on this program, add a line after we've built the graph, right before running the train loop
    writer = tf.summary.FileWriter('./graphs', sess.graph)  # './graphs' is the logs_dir
    print sess.run(x)

writer.close() # close the writer when you'are done using it
