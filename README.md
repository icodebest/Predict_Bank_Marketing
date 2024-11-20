<h2>Bank Marketing Campaign Success Prediction</h2>

<p>The objective of this project is to predict whether a customer will subscribe to a term deposit based on data from the bank's marketing campaigns. The model employs feature selection techniques and various classification algorithms to achieve this goal.</p>

<h3>Steps Performed</h3>

<ol>
    <li><strong>Data Preprocessing</strong>:
        <ul>
            <li>Handled missing values and encoded categorical variables where necessary.</li>
            <li>Standardized the dataset using <code>StandardScaler</code> to ensure consistent model performance.</li>
        </ul>
    </li>
    <li><strong>Feature Selection</strong>:
        <ul>
            <li>Identified the most significant features using techniques such as:
                <ul>
                    <li>Correlation analysis</li>
                    <li>Mutual information</li>
                    <li><code>SelectKBest</code></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Model Training</strong>:
        <ul>
            <li>Trained multiple classification models, including:
                <ul>
                    <li>Logistic Regression</li>
                    <li>Decision Tree</li>
                    <li>Random Forest (Ensemble Method)</li>
                </ul>
            </li>
            <li>Employed 5-fold cross-validation to evaluate model performance and prevent overfitting.</li>
        </ul>
    </li>
    <li><strong>Feature Importance & Impact</strong>:
        <ul>
            <li>Summarized the top features identified during feature selection.</li>
            <li>Analyzed the impact of these features on predicting the success of the marketing campaign.</li>
        </ul>
    </li>
    <li><strong>Evaluation</strong>:
        <ul>
            <li>Compared model performance using metrics such as accuracy, precision, recall, and F1-score.</li>
        </ul>
    </li>
</ol>

<h3>Steps to Clone the Repository</h3>

<p>To clone the repository and run the project, follow these steps:</p>

<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/icodebest/Predict_Bank_Marketing.git</code></pre>
    </li>
    <li><strong>Navigate into the Project Folder</strong>:
        <pre><code>cd Predict_Bank_Marketing</code></pre>
    </li>
    <li><strong>Set Up Virtual Environment</strong>: Create a virtual environment to manage project dependencies:
        <pre><code>python3 -m venv venv</code></pre>
    </li>
    <li><strong>Activate the Virtual Environment</strong>: Activate the virtual environment based on your operating system.
        <ul>
            <li><strong>On Windows:</strong></br><pre><code>.\\venv\\Scripts\\activate</code></pre></li>
            <li><strong>On MacOS/Linux:</strong></br><pre><code>source venv/bin/activate</code></pre></li>
        </ul>
    </li>
    <li><strong>Install Required Dependencies</strong>: Install the required libraries and dependencies listed in the <code>requirements.txt</code> file:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Run the Project</strong>: After setting up the environment, you can run the project file as per your implementation.</li>
</ol>

<p>This structured approach ensures that you can effectively implement and evaluate a predictive model for bank marketing campaign success while maintaining clarity and organization in your code and methodology.</p>
