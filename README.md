•	This project applies multiple data preprocessing techniques to the “Life Expectancy dataset”, preparing it for machine learning tasks. 
  The preprocessing includes missing value handling, categorical encoding, feature scaling, train/test splitting.

•	Missing Value Handling
-	Numerical Features:Imputed using median ,robust to outliers and preserves central tendency.
-	Categorical Features: Imputed using mode or `"Unknown"` to maintain dataset integrity.
-	Observation: No data loss, realistic distributions preserved.

•	Categorical Encoding
-	Label Encoding:Best for binary or low-cardinality features (e.g., `Status`).
-	One-Hot Encoding:Applied to nominal features without natural order.
-	Ordinal Encoding:Preserves ranking for features with natural order.
-	Frequency & Target Encoding: Suitable for high-cardinality features (e.g., `Country`), reducing dimensionality and capturing relationships with `Life expectancy`.
-	Observation:Encoding chosen based on feature type, cardinality, and interpretability.

•	Feature Scaling
-	Min-Max Scaling: Normalizes numeric features to 0–1 range, most effective overall.
-	Z-score Standardization: Centers features around zero, useful for high variance.
-	Vector Normalization (L2) & Max-Abs Scaling: Demonstrated for completeness, less impactful here.
-	Observation: Scaling improves model stability and preserves relationships.

•	Outlier Treatment & Skewness Transformation
-	Skewed features transformed using logarithmic transformation when necessary.
-	No extreme outliers found; aggressive removal not needed.
-	Observation: Minimal transformation preserves natural data structure.
•	Final Justification
-	Preprocessing choices ‘preserve data integrity’, ‘simplify complexity’, and ‘ensure machine learning readiness’.
-	The dataset is now ‘clean, encoded, scaled, and ready for modeling’, balancing robustness and interpretability.
