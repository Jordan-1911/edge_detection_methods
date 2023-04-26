<h2>Edge Detection Methods in OpenCV</h2>

<p>The performance evaluation method I chose to implement uses precision and recall, which are not uncommon metrics used in this field. A ground truth map that represents the true or accurate
Representation of the data against which the results of an algorithm, model, or system are compared to determine their accuracy, reliability and performance. Here, I set the ground truth edges to white (255), and the rest to 0 (black). Next, the precision and recall for each are calculated.</p>

<p>The precision is calculated by the number of true positive edges or correctly detected edges divided by the total number of positive edge pixels detected by the edge detection method. Higher precision means fewer false positives and incorrectly detected images.</p>

<p>Recall is calculated by the number of true positive edge pixels divided by the total number of actual edge pixels in the ground truth. A higher recall means that the method detects more of the actual edges in the images, leading to fewer false negatives or missed edges (Sun et al., 2018).</p>

<p>There are other proposed solutions for ascertaining the quality of edge detection methods. Among the most popular are visual inspection, processing time, confusion-matrix based measures, mean square error (MSE)-based measures, and Figure of Merit (FOM) (Tariq et al., 2021).</p>

<p>In my approach, I created functions to create the synthetic image which created a green circle and square displayed horizontally. Next, various edge detection methods are applied: Canny, Sobel, and Laplacian. Next, noise was added using a RNG and the evaluation function was called again using the new and noisy image. Lastly, the performance metrics were evaluated again and the images were displayed using matplotlib.</p>

<p>The results are as followed:</p>

![Output image of edge detection methods](https://github.com/Jordan-1911/edge_detection_methods/blob/master/Figure_1.png)

<p>References</p>

<p>Sun, W., You, S., Walker, J. G., Li, K., &amp; Barnes, N. (2018). Structural Edge Detection: A Dataset and Benchmark. Digital Image Computing: Techniques and Applications. https://doi.org/10.1109/dicta.2018.8615801</p>

<p>Tariq, N., Rostam Affendi Hamzah, Theam Foo Ng, Shir Li Wang, &amp; Ibrahim, H. (2021). Quality Assessment Methods to Evaluate the Performance of Edge Detection Algorithms for Digital Image: A Systematic Literature Review. IEEE Access, 9, 87763–87776. https://doi.org/10.1109/access.2021.3089210</p>
