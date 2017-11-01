 ## HYPOTHESIS FORMULATION

You should state why your idea is interesting in your report, and what motivates it. 

The Null/Alternatively is formnulate appropriately in accordance with the original question, the significance level alpha should be stated more clearly.


## DATA

The data supports the analysis and seems appropriately pre-processed. The plots should be useful to give a hint of the answer, 
but normalized histograms would enable an intuitive comparison that is impossible in the current plot due to the dramtic difference in absolute counts.

## STATISTICAL TEST

You are testing the mean trip duration. Your dependent variable is continuous and dependent categorical. A common test used in this case is the ANOVA (Analysis of variance). 
or the t-test. However the ANOVA and t-tet are parametric tests: they assume the IV follows a Normal distribution. This is obviously not the case for your variable, as the plots show. 
In practice, ANOVA would be commonly used for this analysis. Better, non-parametric choices, would be the 
Mood’s median or Kruskal-Wallis test (https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.median_test.html).




NOTE: For whichever test you chose, you want the one-tailed version


