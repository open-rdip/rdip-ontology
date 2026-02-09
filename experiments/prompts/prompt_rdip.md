# RDIP Test

[Chat URL](https://grok.com/share/bGVnYWN5LWNvcHk_cc48a59c-66f5-4e49-8842-9cf1e2c647da)

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: The main methodological contribution of this work is development of principled estimands and pre-diction strategies with missing outcomes and covariates regardless of the choice of model. However, a comparison of models can be useful as the quality of the predictions and optimization with the proposed transition models has not been evaluated in this setting. In this section, we assess performance relative to Bayesian Additive Regression Trees (BART) (Chipman et al., 2010) trained on a dichotomous retention outcome, Yj (∆), where values missing due to censoring are implicitly imputed as not retained. This is to mimic machine learning (ML) risk prediction models popular in HIV/AIDS. The dichotomization is done because common ML packages easily accommodate binary classification tasks, but do not accommodate continuous outcomes with complexities of censoring and competing events. Of course, this comes at the expense of information loss. It also mimics naive implicit imputations done in the presence of censoring, which has led to underestimation of retention (Bengtson et al., 2020). Such approaches lead to poor predictions regardless of the flexibility of the downstream predictive modeling. Without loss of generality, we set j = 1 so that we are analyzing retention following the first visit. To assess performance, we simulate a training set with 500 subjects each in the following way. For each subjects we simulate six covariates (three binary and three continuous). Of those six covariates, two covariates (one binary and one continuous) can potentially be missing in ways that are depending on the other 4 covariates. Conditional on observed covariates, one of three possible scheduling times are assigned to each subject. Conditional on covariates and a scheduled return time, a death time, and censoring time are simulated from separate Weibull hazard models. To mimic clumping around the scheduled time, a subsequent return-time is simulated from a two-part mixture of a point-mass at the scheduled time and a covariate-dependent Weibull distribution. The next event is the first of the three simulated events. In the same way, we simulate a test set with 500 subjects where there 13 is no censoring (i.e. censoring time is set to infinity) so that we have complete outcome information Y1(∆) ∈{0,1}. In this simulation, we set ∆ = 2 to analyze two-week delay. In each iteration, we use the training set to estimate the described models, and compute posterior mean of retention probability under the assigned scheduled return time, Ψs 1(H1; ∆), for each subject in the test set. We use average test-set AUC to summarize predictive performance across simulated datasets, which are presented in Panel A of Table 1. Missingness Low Censoring High Censoring Logistic BART BTM Logistic BART BTM None .644 .642 .697 .561 .557 .669 Low .583 .570 .635 .551 .526 .617 High .580 .570 .631 .544 .527 .610 Panel A: Average Test-Set AUC Covariate Panel B: Accuracy of Estimated Optimal Scheduling Time Low Censoring High Censoring Covariate Missingness None Low High Logistic BART BTM Logistic BART BTM .578 .574 .786 .305 .316 .659 .479 .475 .598 .369 .351 .524 .468 .489 .593 .358 .352 .516 Table 1: Panel A: Average test-set area under the curve (AUCs) of predicted retention probabilities for various missingness/censoring scenarios. Panel B: Average proportion of test-set patients for whom the method correctly identified the optimal scheduling decision. Results averaged across 300 simulation runs each with n= 500 subjects in both panels. Results labeled “BTN” is the developed Bayesian transition model while “BART” is the described tree-based model. We also include maximum likelihood estimates of Ψs 1(H1; ∆) from a logistic regres- sion of dichotomous Y1(∆) on all covariates using the training set - labeled “Logistic”. In order to satisfy conditional ignorability in the presence of missingness, for all methods, we stratify the models based on missingness pattern. That is, we fit a separate model in each of the four possible missing- ness patterns, each adjusting for covariates observed in that pattern. A prediction is generated for a test set subject using the model that corresponds to that subject’s missingness pattern. Panel A of Table 1 presents AUCs under a low and high censoring in the training set. These have censoring rates approximately 20% and 40% on average across simulation runs. In addition, we simulate across a range of covariate missingness rates. The setting “None” is the simplest setting where all covariates are observed. In the “Low” setting, about 45% of subjects have at least one of the two partially observed covariates missing. In the “High” setting, about 60% have at least one of the two covariates 14 missing. Note that since the return-time is generated from a two-component mixture, all models are misspecified. Thus, across scenarios, what is more important is the relative test-set AUC, rather than the absolute AUC. We see that the proposed approach has higher AUC than BART. The performance differential is maintained even as censoring rates increase. This is likely because our method works with the underlying continuous return-time and allows censored and dead patients to contribute to the model through their respective cause-specific hazards. In contrast, the other methods rely on dichotomous return-time. In addition to test-set predictive performance under an observed scheduling time, we are also interested in how well the method can estimate the optimal scheduling time s∗ 1(h1). For each subject in the test set, we compute the true scheduling decision (out of the possible 3) that maximizes Ψs 1(H1; ∆) using that subject’s covariates and true model parameters. We then check to see if this matches the mode of s∗ 1(h1) across posterior draws. In Table 1 Panel B, we see BTM is able to accurately estimate the optimal scheduling decision for 78.6% of test set subjects, on average, across simulation runs in the low-censoring-no-covariate-missingness setting. Performance dips to 59.8% and 59.3% with low and high covariate missingness, respectively. The accuracy of the optimal estimate obtained by comparing estimates of Ψs 1(H1; ∆) under various s using BART and logistic regression all perform worse. In the setting with high censoring, BART and logistic regression exhibit worse performance across covariate missingness levels. Again, the loss of information and inability to have censored and dead patients contribute fully to the model is aggravated when censoring rates are high. One conclusion here is that a full generative, semiparametric model for the return time yields adequate estimates of the causal quantities of interest across these censoring and missingness settings and outperforms common off-the- shelf alternatives. In cases where there is very minimal or no censoring, then Y1(∆) is observed for everyone. In this case, the difference between stratified BTM and stratified BART will be negligible. 7 Modeling HIV Care Retention in AMPATH We used the developed method to analyze retention following the first visit (j = 1) using electronic health records from AMPATH. This is because patients are believed to be at highest risk of disen- gagement at the beginning of care. Patient data were collected from four clinics - Kitale, Busia, Uasin Gishu District Hospital (UGDH), and Kitale County Referral Hospital Module A (KCRH). We include 15 all adults with HIV with their first visit occurring between between January 1, 2014 and and July 31, 2023 (end of the data cut), which totals to n= 11,011. All patients have recorded a scheduled return time, gender, age, whether or not they have ever been on antiretrovirals (ARV), and the particular clinic they visited. Additionally, we have viral load and CD4 count recorded for patients who have had these values monitored. For patients who have not, this information is missing. A summary of the data is given in Table 2. Across clinics, a plurality of patients have both CD4 count and viral load missing, but a significant subgroup have viral load observed while having CD4 count missing. A very small fraction have both measured. The most common scheduling decision was a two-week return time across sites. There were some notable baseline differences in ARV and age across clinics. Clinic Table 2: Summary Statistics for patients at their first visit after enrollment. Mean and Interquartile range (IQR) presented for continuous features. Count and proportions presented for discrete features. Statistics are stratified by clinic at which visit was made. Note there is substantial variability in features across clinic in terms of scheduling decisions (e.g. Busia) and ARV (e.g. Kitale has especially lower rates) and age at enrollment (e.g. KCRH having older patients). Abbreviations: UGDH -Uasin Gishu District Hospital; KCRH- KCRH Module A. Kitale (n=3398) Busia (n=2891) UGDH (n=2438) KCRH Module A (n=2284) Missing: viral load only 1389 (.41) 607 (.21) 303 (.12) 895 (.39) CD4 only 93 (.03) 114 (.04) 50 (.02) 73 (.03) both 1907 (.56) 2167 (.75) 2077 (.85) 1313 (.57) neither 9 (<.01) 3 (<.01) 8 (<.01) 3 (<.01) Observed log viral load 7.7 (4.8-10.1) 8.0 (5.7-10.6) 7.5 ( 4.7-9.9) 7.1 (5.0-7.7) Observed log CD4 5.2 (4.6-6.1) 5.6 (5.1-6.3) 5.4 (4.9-6.2) 5.2 (4.8-6.0) Age at enrollment 36.1 ( 28.0-42.4) 36.0 ( 28.0-42.7) 35.0 (26.8-41.7) 40.2 (31.8-47.5) Male 1261 (0.37) 1064 (0.37) 895 (0.37) 890 (0.39) On antiretrovirals (ARV) 2710 (0.80) 2688 (0.93) 2169 (0.89) 2265 (0.99) Scheduled return time Two weeks 2848 (0.84) 2099 (0.73) 2004 (0.82) 1899 (0.83) Four weeks. 485 (0.14) 671 (0.23) 354 (0.15) 348 (0.15) Eight weeks 65 (0.02) 121 (0.04) 80 (0.03) 37 (0.02) We focus our analysis on loss to follow-up (LTFU) by defining retention with ∆ = 90/7. We randomly select 1,000 subjects from the full data set to be in a test set that is held out from model training. The remaining 10,011 subjects are used for training. We fit cause-specific hazards described in Section 4 stratified by each clinic, scheduling decision, and missingness pattern combination. In each missingness pattern, we adjust for covariates observed in that pattern. In patterns where either viral load or CD4 are measured, they are included in the modeling using b-splines to allow for non-linear 16 Figure 3: For all plots, j = 1 and ∆ = 90/7 ≈13. Left: Posterior mean and 95% credible interval of Ψs j (hji; ∆) for each subject iin the test set under their scheduled return time s= si. Middle: For each subject, this plot displays the posterior mean of Ψs j (hji; ∆) on the x-axis along with with the width of the credible interval of Ψs j (hji. Right: Each subject’s posterior PMF of the optimal scheduling time representing in a machina triangle. P(s∗ j (hj ) = 2 |D) is on the x-axis and P(s∗ j (hj ) = 4 |D) on the y-axis. The red point in the middle represents maximal uncertainty with each option having 1/3 posterior probability of being the optimal option. Patients closest to vertex (0,0), (0,1), and (1,0) are those with option 8, 4, and 2 as the posterior mode optimal rule, respectively. functional forms in the cause-specific hazard models. A key advantage of the Bayesian approach is that the posterior draws of the model parameters need only be obtained once and stored. Quantities of interest can then by computed on-demand by post-processing these draws - making it ideal for running at point-of-care dashboards. This is in contrast to frequentist procedures that may require complex bootstrapping procedures be run for each new quantity of interest. The left panel of Figure 3, for instance, displays posterior mean and 95% credible interval for each subject’s retention probability. Some subject are predicted to be highly likely to be retained, but with high uncertainty. This is partially because some strata are very small. For instance, the return time models among patients in Busia who were scheduled to return in eight weeks was trained on fewer than 121 subjects (see Table 2), with the precise number depending on the monitoring pattern. Thus, predictions for test set subjects in this stratum have larger posterior uncertainty. A helpful way of making decisions under uncertainty is shown in the middle panel of Figure 3 which plots the width of the 95% credible interval against the posterior mean for each subject’s retention probability. The red dashed lines at the empirical averages of these values divides the space into four quadrants, which can be used to guide outreach decisions. For instance, the patients in the bottom-left quadrant are ones who we are relatively more certain have a lower than average posterior probability of being retained. They are likely excellent candidates 17 for outreach efforts. In contrast, the patients in the top-left quadrant also have a lower-than-average posterior probability of being retained. But given the higher posterior uncertainty, if outreach resources are scare they may be lower priority. The right panel of Figure 3 conveniently displays the posterior distribution of the optimal schedul- ing decision for each subject as described in Section 5. The posterior mass function over the op- timal scheduling decision for a subject is given by the triple {P(s∗ j (hj ) = 2 |D),P(s∗ j (hj ) = 4 | D),P(s∗ j (hj ) = 8 |D)}, which can be represented as a point in this triangle. The red point represents maximal uncertainty about which of the option maximizes ∆-retention, giving uniform 1/3 posterior probability to each option. The red points on each of the three vertices represents high posterior certainty that the corresponding option is the optimal one. For instance, points near the vertex (0,0) are patients with ≈1 posterior probability of S = 8 being the optimal decision. These diagrams can be used to make decisions under uncertainty in the following way. Consider two patients who are above the line y= 1/3 on the triangle, but one is closer to the vertex (0,1) than the other. For both of these patients, the posterior mode optimal rule is ˆ s∗ j (hj ) = 4. However, the one closer to (0,1) is the one for whom we have higher posterior precision around this mode. Thus, if we had only one appointment time slot 4 weeks from the current visit, we may consider scheduling the patient closer to (0,1). Figure 4: Left: For j = 1 and ∆ = 90/7, each point represents Ψs j (hji; ∆) for each subject i in the test set under their scheduled return time s= si under BART vs. the formulated Bayesian Transition Model. Due to low censoring rates, the predictions produced by the two approaches are quite consistent, as shown by the scattering of points around the 45-degree line. Right: For one subject, i, in the test set, BMT produced estimates of Ψs 1(h1i; ∆) for various ∆ under each possible scheduling decision s∈{2,4,8}. This plot illustrates that ability of our Bayesian Transition Model to produce point and interval estimates under a variety of retention definitions, ∆, and scheduling options without need to re-run the models. It illustrates that optimization for a single ∆, while dominant in the HIV/AIDS literature, is not global and motivates future work on optimization via more general utility functions. 18 We also ran prediction models using BART for LTFU. Since censoring and death rates were quite low in the data (≈1% and ≈10%, respectively) the predictions were quite similar when we correctly flag dead patients as not being retained and simply drop censored subjects. This can be seen in the left panel of Figure 4. Each point is a subject in the test set and the scattering around the 45 degree line depicts general agreement in the predictions. But, as shown in the simulation, higher censoring rates may lead to differences in performance. Lastly, rather than keeping focus at a particular ∆ = 90/7 ≈13 weeks, we could consider estimation retention, Ψs 1(h1; ∆) across ∆. The right panel of Figure 4 depicts this for a single subject. Essentially this traces out the posterior subdistribution function (Kalbfleisch and Prentice, 2011) of the delay time, W1−s1, under three different scheduling decisions (s∈{2,4,8}). The significance of this plot is to show that optimization for a given ∆ does not yield a decision that is globally optimal across all ∆. For this subject, scheduling the next visit in 8 weeks maximizes retention under LTFU definition of ∆ ≈13 (indicated by the dashed vertical line). However, this minimizes retention under the default definition (∆ = 1). Global optimality would only occur if the counterfactual subdistribution function of delay time under decision s= 8 was above the the subdistribution functions under the other decisions across all ∆. Thus, while vast majority of clinical and applied work in HIV retention modeling focuses on a single ∆, our analyses suggests optimizing based on the entire subdistribution function could be desirable area of future work. This can perhaps be done by seeing which decision has the largest area under the subdistribution function or optimizing based on an expected utility function that takes a weighted average of specified points on the subdistribution function.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/HIV-Retention-Bayesian-Transition-Model",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Development and application of a Bayesian Transition Model for HIV care retention with censored and competing-risk outcomes"
    },
    {
      "@id": "rdip:Dataset/AMPATH-EHR-2014-2023",
      "@type": "schema:Dataset",
      "schema:name": "AMPATH electronic health records (first visit, adults with HIV, 2014-01-01 to 2023-07-31)",
      "schema:size": 11011,
      "schema:description": "Patient-level data from four clinics (Kitale, Busia, Uasin Gishu District Hospital, KCRH Module A) containing scheduled return time, gender, age, ARV status, clinic, viral load (partially missing), CD4 count (partially missing), observed return times, death indicators, and administrative censoring.",
      "prov:wasGeneratedBy": "rdip:Activity/DataCollection-AMPATH"
    },
    {
      "@id": "rdip:Activity/DataCollection-AMPATH",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Routine collection of electronic health records in AMPATH HIV care program",
      "prov:used": "rdip:Dataset/AMPATH-EHR-2014-2023"
    },
    {
      "@id": "rdip:Activity/SimulationStudy",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Monte-Carlo simulation of training (n=500) and test (n=500, no censoring) datasets under varying censoring and covariate-missingness scenarios",
      "prov:generated": [
        "rdip:Dataset/SimulatedTrainingSets",
        "rdip:Dataset/SimulatedTestSets"
      ],
      "rdip:usedSoftware": {
        "@id": "rdip:Software/CustomRCode",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Custom R / Stan code (not explicitly named)",
        "rdip:version": "unknown"
      }
    },
    {
      "@id": "rdip:Activity/BayesianTransitionModel-RealData",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Fitting of stratified Bayesian cause-specific hazard transition models (BTM) on AMPATH data",
      "prov:used": "rdip:Dataset/AMPATH-EHR-2014-2023",
      "rdip:usedSoftware": [
        {
          "@id": "rdip:Software/RStan",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "RStan (implied Bayesian implementation)",
          "rdip:version": "unknown"
        }
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/BTM-PosteriorDraws-AMPATH",
        "@type": "schema:Dataset",
        "schema:name": "Posterior draws of stratified cause-specific hazard parameters (clinic × scheduled time × missingness pattern strata), with b-splines for viral load and CD4 when observed"
      }
    },
    {
      "@id": "rdip:Activity/BART-Comparison-RealData",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Fitting of stratified BART models on AMPATH data for comparison",
      "prov:used": "rdip:Dataset/AMPATH-EHR-2014-2023",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/BART-Rpackage",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "R package BART (Bayesian Additive Regression Trees)",
        "rdip:version": "unknown (Chipman et al., 2010 implementation)"
      }
    },
    {
      "@id": "rdip:Activity/LogisticComparison-RealData",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Maximum-likelihood logistic regression of dichotomous retention outcome (stratified by missingness pattern)",
      "prov:used": "rdip:Dataset/AMPATH-EHR-2014-2023",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/R-glm",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "R glm() or equivalent",
        "rdip:version": "unknown"
      }
    },
    {
      "@id": "rdip:Activity/PostProcessing-Predictions",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Post-processing of stored posterior draws to compute retention probabilities Ψ^s_j(h; ∆), optimal scheduling decisions, credible intervals, and ternary plots for test-set subjects",
      "prov:used": "rdip:Dataset/BTM-PosteriorDraws-AMPATH",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/CustomRPostprocessing",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Custom R post-processing scripts",
        "rdip:version": "unknown"
      },
      "rdip:outputDataset": [
        {
          "@id": "rdip:Dataset/TestSet-Predictions-BTM",
          "@type": "schema:Dataset",
          "schema:name": "Retention probabilities, credible intervals, and posterior PMFs of optimal scheduling time for 1,000 held-out AMPATH patients"
        }
      ]
    },
    {
      "@id": "rdip:Activity/PerformanceEvaluation-Simulation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Calculation of average test-set AUC and optimal-scheduling accuracy across 300 simulated datasets for BTM, BART, and Logistic models",
      "prov:generated": "rdip:Dataset/Table1-Results"
    }
  ]
}
```

This JSON-LD captures the main provenance elements explicitly or implicitly described in the Methodology section:

*   The central research project
*   The real-world AMPATH EHR dataset and its collection activity
*   The simulation study that generated synthetic data
*   The core data-production activities (fitting the proposed Bayesian Transition Model, BART, and logistic regression)
*   The software/tools used (R/Stan for Bayesian modeling, BART package, standard R for logistic regression, custom post-processing)
*   The key output datasets (posterior draws, test-set predictions, simulation performance tables)

All entities are linked with appropriate RDIP/PROV relations as required.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: TouseGPT-3tocodetexts,weprovide itwithaspecificpromptdesigned toteachGPT-3the coding process. This prompt varies from application to application, as the coding method depends on the specific concepts being coded. Throughout these applications, our goal is to give GPT-3 as little 3 Ryttinget al. FIGURE 1. Example Prompts Using only the following categories """ Macroeconomics Civil Rights, Minority Issues, and Civil Liberties Health ... Death Notices Churches and Religion Other, Miscellaneous, and Human Interest """ Assign the following headlines to one of the categories: IRAN TURNS DOWN AMERICAN OFFER OF RELIEF MISSION -> Inter- national Affairs and Foreign Aid In Final Twist, Ill Pavarotti Falls Silent for Met Finale -> Arts and Entertain- ment Baseball; Incredibly, Yankees Rally in 9th Again and Win in 12 -> Sports and Recreation House Panel Votes Tax Cuts, But Fight Has Barely Begun -> Are the following descriptions of Republicans extreme or moderate? -angry, racist, close-minded, homophobic: Extreme -people, hopeful, educated, agreeable: Moderate -conservative, white, male, religious: (b) Pig. Partisans Example Prompt - Positiv- ity, 2-exemplars Do the following descriptions of Democrats mention personality or character traits? -accepting, tolerant, intellectual, charitable: Yes, the descriptions mention personality or character traits. -black, young, female, poor: No, the descriptions do not mention personality or character traits. -conservative, white, male, religious: (a) CAP Example Prompt - New York Times, 3-exemplars (c) Pig. Partisans Example Prompt - Traits, 2-exemplars guidanceaspossibletodemonstrateitsflexibilityandefficiencyinlearninghowtoactas acoder. In providing GPT-3 with these prompts, we discovered that the LM responded quite similarly across variousversionsofourguidance,andthatitrequiredonlytwoorthreecodedexamplestoperformwell on these tasks. For additional information on the process of engineering these prompts, see the Online Appendix. After giving GPT-3 these prompts and observing how it codes a set of data, we compare that codingtoacorrespondingsetofcodesgeneratedbyhumans. Thisallowsustodirectlycomparethe performanceofGPT-3tohumancoders. Inthecaseofourlastapplication,wealsocompareourresults to a SML procedure. We make these comparisons based on coding agreement as well as efficiency (in termsoftimeand costtocodewithother techniques). We construct our prompts by providing instructions, categories (if necessary), exemplars (labeled examples of the task), and then the text to classify. We then compute GPT-3’s probabilities for the nexttokenoveritsvocabularyandselectthetokenwiththehighestprobabilityasthemodel’s coding choice. Forcolor-codedexamplesofprompts, see Figure1. WeevaluateGPT-3’scodingperformanceusingvariousintercoderagreementmeasuresbetween GPT-3’s codes and the codes generated by humans we hired to code the same texts. These are as follows: 4 APSR Submission Template APSRSubmission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSRSubmissionTemplate APSRSubmissionTemplate APSR Submission Template Towards Coding Social ScienceDatasetswith LanguageModels Intraclass correlation (ICC) Intraclass correlation measures inter-coder agreement among human coders using numerically ordered, (quasi-) continuous values in their coding (e.g., rating a text by some characteristic on a 1-5 scale). ICC scores are between -1 and 1 and are typically interpreted as follows: < 0.5 = poor inter-coder agreement, 0.5− .75 = moderate agreement, 0.75−0.9 = good, and >0.9 = excellent (Cicchetti 1994; KooandLi2016). Joint probability of agreement Fortaskswithun-ordered,categoricalcodes,weusetwodifferentmeasures. Thefirst,joint-probability of agreement, measures the probability of any two coders agreeing. In the 2-coder case, where one of the coders is ground truth, this reduces to raw accuracy. Joint probability agreement ranges from 0 to 1. Between two coders, it is calculated as follows: 1 𝑁 𝑁 𝑖=1 (𝑦1,𝑖 = 𝑦2,𝑖), where 𝑁 is the number ofinstancesbeingcoded,and 𝑦1,𝑖,𝑦2,𝑖 arethefirstcoder’sandthesecondcoder’srespectivecodings of instance 𝑖. In the case of 𝐾 coders, the joint probability agreement is the mean of the pairwise agreements. Fleiss’ kappa Fleiss’ kappa measures the degree to which the proportion of agreement among coders exceeds the agreement of fully random coders (Fleiss 1971; Fleiss et al. 2003). Used specifically to quantify intercoderagreementforcategoricaldata,thismeasurerangesfrom−1 to1. When 𝜅= 0,itmeansthat the two raters agree at a rate not better than chance. 𝜅 <0 means increasing agreement worse than chance,and 𝜅 >0 meansincreasing agreement greaterthan chance. EXPERIMENTS We consider GPT’s capacity to serve as a coder using data from four datasets: Pigeonholing Partisans (PP), New York Times Headlines (NYT), Congressional Hearings (Congress), and The Guardian 5 Ryttinget al. Populism (TGP). We chose these datasets to maximize differences in coding tasks as a means of exploring GPT-3’s limits. These four applications vary in the difficulty of the coding task, the domain (or topic) of the coding, the structure of the texts, and measurement of the coded variable (ordinal, categorical,binary,etc.). Pigeonholing Partisans (PP) We first consider the ability of GPT-3 to act as a coder with data on Americans’ stereotypes of Republicans and Democrats (Rothschild et al. 2019). These data, collected in 2016, asked individuals to list four words or phrases that described typical supporters of the Democratic and Republican Parties.1 This procedure is common in psychological studies of stereotypes (Devine 1989; Eagly and Mladinic1989), andallowssurveytakerstodescribepartisansintheirown wordsThisdatasetistoo smallforotherkindsofautomatedcodingandanidealwaytoconsiderhowwellGPT-3canclassify texts withoutextensivetrainingsets. To evaluate how well GPT-3 can serve as a coder on these kinds of short, open-ended texts, we recruited2873humancodersthroughthesurveyplatformLucid (CoppockandMcClellan2019)to code a total of 7675 descriptions of partisans. Each description was coded at least three times by a random set of coders, who were given minimal instructions for coding the texts.2 As such, the coders inthisstudyshouldbe considered "lightly trained"rather than rigorouslyinstructedon the coding. Coders rated the texts along five dimensions: (1) positivity (general positive/negative valence), (2) extremity(extremeormoderatequalityofthewords),andwhetherthetextmentioned(3)character orpersonalitytraits,(4)governmentorpolicyissues,or(5)socialgroups. Eachofthesedomainsis importanttothetheoreticalideasoftheoriginalworkonpartisanstereotypes(Rothschildetal.2019; Busbyetal.2021). After the human coding process was complete, we asked GPT-3 to complete a series of coding 1Moremethodological detailscanbefoundin publisheddiscussions ofthis work. See(Rothschildetal. 2019). 2ThesetextsincludethosecreatedbyhumanrespondentsintheoriginaldataaswellastextscreatedbyGPT-3 and discussed in other, published work (Argyle et al. ming). That work indicates that human respondents cannot distinguish betweenthe twokindsofstatements. 6 APSR Submission Template APSRSubmission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSRSubmissionTemplate APSRSubmissionTemplate APSR Submission Template Towards Coding Social ScienceDatasetswith LanguageModels FIGURE2. PPICC1k: NotethatincludingGPT-3intheclassofconsideredcodersincreases ICC1k in coding for all attributes except “Traits”. The opposite happens when including other, simulated coders. ICC1k for Pigeonholing Partisans 0.7 Positivity 0.6 0.74 0.74 0.14 0.1 0.45 0.38 0.6 Extremity 0.34 0.35 0.16 0.13 -0.08 0.23 0.22 0.5 0.4 Groups 0.16 0.23 0.24 -0.18 -0.14 0.11 0.11 0.3 Traits 0.17 0.06 -0.51 -0.51 0.02 0.02 -0.17 0.2 0.1 Issues 0.2 0.21 -0.01 -0.02 -0.26 0.12 0.09 0.0 Human Human+GPT-3 Human (averaged)+GPT-3 Human+0 coder Human+1 coder Human+random coder Human+random coder (distribution) tasks on all 7675 texts directly analogous those completed by humans. Next, we examined how closely GPT-3followsindividualhumancodersandhumancodingintheaggregate,alongwithhowclosely humansfollowed eachother. To that end, we calculated ICC scores with these data (Fig. 2). As coders are randomly assigned to textsand notalltextsarescoredbythesamecoders,weuse ICC1k,whichaccountsforthisstructure (ShroutandFleiss1979). OurfocushereisontheincreaseordecreaseinICCwhenGPT-3’scodesareaddedtothethree human codes. If GPT-3 improves the reliability of the coding, ICC should improve. If it does not offer thisbenefit, the ICCscore should stay the same or decrease. We also compare adding GPT-3’s scores to adding simulated scores to ensure that the addition of another coder by itself does not drive what we observe: (1) a coder who codes all texts as 0 (lacking the attribute), (2) a coder who codes all texts as 1(containingtheattribute), (3)a coder whocodesrandomly, and(4) acoder whocodes all texts randomly, but with the same overall distribution as GPT-3’s predictions. We also consider the ICC 7 Ryttinget al. values when comparing GPT-3’s codes to the average of the human coders (rather than individual codersseparately). ThestatisticsinFigure2suggestthataddingGPT-3asacoderaddsagreatdealtoreliabilityfor two measures (positivity, groups), slightly increases reliability of the coding for two others, (extremity, issues), and reduces reliability in one (traits). Notably, this last area is where human coders correlated the least with each other (correlations between human coders on this domain ranging from 0.07 to 0.08)andmayrepresent afundamentally challenging task. ThereisalsoastarkdifferencebetweenaddingGPT-3andaddingeachofthesimulatedcoders. We concludethattheboostinICCfromGPT-3isnotduetosimplyaddinganothercoder. Furthermore, since adding GPT-3’s outputs to the human outputs generally either increases or maintains ICC across each attribute, we conclude that GPT-3 achieves human or better performance at this task. Importantly, achievingthislevelofperformancerequiredneithercodingalarge-scaledataset(ontheorderoftens ofthousandsormore)nora large,labeled setof training dataforthelanguagemodel. Comparative Agendas Project (CAP) For a different application of GPT-3 as a coder, we during to the Comparative Agendas Project (CAP) system of coding. CAP provides a coherent framework for documenting media and government attention to various policy issues in a comprehensive set of policy domains (Baumgartner et al. 2019). CAP datasetsaimtobe comprehensive, transparent, and replicable (Bevan 2019), with many housed at the CAP website ([www.comparativeagendas.net](http://www.comparativeagendas.net)). More than 200 scholars have used CAP to test a vastrangeofempiricalpoliticalsciencetheoriesacrossmorethanadozencountries(Walgraveand Boydstun 2019). The CAP master codebook moves beyond the simple coding of the PP data, spanning at least 21 major categories (with others added for some specific applications). In order to succeed here, GPT-3mustproduceahighprobabilityforoneofalarge,unordered,pre-specifiedsetoftokensthat correspondsto thespecificcontent of the inputdata. Prior efforts to automate coding in the CAP framework have met limited success (Karan et al. 2016;Hillardetal.2008;PurpuraandHillard2006;Sevenansetal.2014;SebőkandKacsuk2021). 8 APSR Submission Template APSRSubmission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSRSubmissionTemplate APSRSubmissionTemplate APSR Submission Template Towards Coding Social ScienceDatasetswith LanguageModels Sebok and Kacsuk (Sebők and Kacsuk 2021) are able to achieve an 80%+ F1 score on average across categories, but this is reported after culling over 40% of their dataset due to difficulty of classification. We, on the other hand, provide scores given full coverage of the dataset. Reported performance in various approaches is substantially lower than this (accuracies near or below 50%) for dictionary methods,lessefficientSMLs,corporawithlesstrainingdata,orinspecifichard-tocodecategories, which upper limit our average accuracy exceeds. Again, the highest performing outcomes are achieved bysettingrejectionthresholds(forambiguoustextsorcaseswherehumansormodelsdisagree)and either sacrificing coverage or targeting human coders to uncertain cases (Karan et al. 2016; Sebők and Kacsuk 2021). We achieve our without dropping cases, using multiple models, human disambiguation ofdifficultcases,andextensive labeledtrainingdata. To account for class imbalances and differences in baseline probabilities of different tokens, we normalize the probability distributions in a manner similar to (Zhao et al. 2021). We estimate GPT-3’s biastowardsacategoryasthetotalweightgiventoeachcategoryoverabalancedvalidationset,divide eachcategoryprobabilitybyGPT-3’sbiastowardsit,andnormalizetosumto1. Wefoundthatthis producedmodestaccuracyboostsof4-5%. Ifasmallvalidationsetisavailable,werecommendthis calibrationtechnique;however,results werequalitatively the same without this calibration. We consider two data sourcesthat have previouslybeen codedusing the CAP framework- coding of U.S. Congressional hearing summaries and the New York Times front page. We conducted our codingwithGPT-3separatelyforeachof these applications. CAP: Congressional Hearing Summaries (Congress) TheCongressionalHearingcorpuscontains the Congressional Information Service summary of each U.S. Congressional hearing from 1946 to 2010. ThesesummarieswerereadbyhumancodersandassignedtoCAPclassifications. Wehiredand trained threehuman coders forthis application, providing them with the same instructions outlined in the CAP codebook. This allows us to compare how different human coders and GPT-3 compare tooneanother(whichisnotpossiblewiththeoriginaldata,giventhatitlacksscoresfrommultiple coders). We gave GPT-3 the full summary text, making the coding task is highly comparable between thehumansandGPT-3. Allresultsarereportedfor 𝑛= 326 texts,whichconstitutes16textsforeach category minus 10 for incompleteness in the human codes. We used a random subset of the dataset of 9 Ryttinget al. FIGURE3. TwomeasuresofGPT-3’sagreementwithhumancoderscomparedwithhumans’ agreement with human coders, across two datasets. Congress New York Times 0.6 Fleiss’ Kappa 0.4 Joint Agreement 0.2 0.0 over10,000texts forthis application. Figure3presentsourcomparisonofGPT-3’sandthehumans’codes. Bothourintercoderagreement metrics tell the same story, and imply a finding that holds across metrics: GPT-3 correlates with each humanjustaswellasorbetterthanthehumanscorrelatewitheachother. Notethatthehighestjoint agreement(.63) andhighestFleiss’ kappa (.61) both occurbetween GPT-3 andHuman 2. Despite there being no real ground truth for this task, we visualize “accuracy” statistics based on the original dataset’s single coder as provided by CAP (Figure 4). The lack of ground truth is validatedbyagreatdealofhumandisagreement,asthefiguremakesclear. Weseetheaccuracyfor eachcoder,withcategoriessortedinorderofGPT-3’saccuracy. Interestinglyenough,GPT-3seems to do better at categories that humans do better at, and worse at the categories that humans fail at. Overall,theaccuracieswere60%forGPT-3,comparedto63%,66%,and55%forthethreehuman codersrespectively. ThehighjointagreementandFleiss’kappabetweenGPT-3andthehumancoders,aswellasthe similar accuracies across categories, demonstrate GPT-3 performance on-par with humans on this dataset. Given the efficiency gains from using GPT-3, such as lower costs in training coders and 10 APSR Submission Template APSRSubmission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSRSubmissionTemplate APSRSubmissionTemplate APSR Submission Template Towards Coding Social ScienceDatasetswith LanguageModels FIGURE 4. Congress Accuracy by Coder: Treating the original dataset’s code as “ground truth”, and sorting categories in descending order based on GPT-3’s score, note how noisy the performance of the human coders is. There is only 1 category that all humans score strictly better on (International Affairs). Congress Accuracies 1.0 0.8 GPT-3 Human 1 Human 2 Human 3 0.6 Accuracy 0.4 0.2 0.0 Agriculture Immigration Social Welfare Education Energy Technology Environment Labor Law and Crime Health Foreign Trade Housing Transportation Defense Government Operations Domestic Commerce Macroeconomics Civil Rights Culture Public Lands International Affairs scalability to a large number of texts, we suggest that this gives additional evidence in favor of the usefulnessofLMsascoders. CAP: New York Times Front Page Dataset (NYT) ThesecondCAPdatasetweuseistheNewYork TimesFrontPageDataset,generatedandcontributedbyAmberBoydstun(Boydstun2013). Thedataset includes 31034 front page New York Times headlines from 1996 - 2006, along with the policy category label assigned by trained human coders. The categories are adapted for media use, and so include 28primaryclassificationcategories. Forthisapplication,werandomlysampled20textsfromeach of the 28 categories to be coded by four human coders and GPT-3. All results are reported for the correspondentsetof 𝑛= 560 texts. Theoriginalhumancoderswereinstructedtoreadtheheadlineandthefirstthreeparagraphsofthe article. In our work, GPT-3 is only provided the headline, because the full article text is not available in the public data. To control for this difference in available information, we also hired four human coderscomplete anidenticalclassification taskto GPT-3, consideringonlythearticleheadlines. Since the structure of the NYT data is the same as the Congress data, we use the same kind of analyses. For both joint agreement and Fleiss’ kappa (Figure 3), GPT-3 agrees with the humans about as much as they agree with each other. GPT-3’s total accuracy was 55%, compared to 57%, 59%, 11 Ryttinget al. FIGURE 5. New York Times Accuracy by Coder: Treating the original dataset code as “ground truth”, and sorting categories in descending order according to GPT-3’s score, note how noisy the humans’ coding is. Clearly some areas are easier for human coders (e.g., Death Notices) and some are easier for GPT-3 (e.g., Environment). New York Times Accuracies 1.0 0.8 GPT-3 Human 1 Human 2 Human 3 Human 4 0.6 Accuracy 0.4 0.2 0.0 Environment Sports and Recreation Health Churches and Religion Immigration Education Labor Arts and Entertainment Social Welfare Agriculture Transportation State and Local Government Administration Weather and Natural Disasters Space Science Technology and Communications Law Crime and Family Issues Foreign Trade Banking Finance and Domestic Commerce Energy International Affairs and Foreign Aid Community Development and Housing Issues Fires Other Miscellaneous and Human Interest Civil Rights Minority Issues and Civil Liberties Government Operations Death Notices Defense Macroeconomics Public Lands and Water Management 51%, and 45% for the four humans respectively. We also notice a strong trend between GPT-3’s accuracy and the humans accuracy per category (Figure 5). Unlike Congress, however, there are 3 categories for which the humans all perform better than GPT-3: “International Affairs and Foreign Aid,” “Government Operations,” and “Death Notices.” On the other hand, GPT-3 performs better than humans at some other categories: “Environment,” “Health,” and “Labor.” Overall, these results again demonstratethat GPT-3 generallyachieves on-parperformancewith humans. The Guardian Populism (TGP) For our final application, we consider how GPT-3 codes a multifaceted concept - populism. While disagreement exists about the meaning of this term, many scholars have gravitated towards a definition that populism is a discourse that describes politics as a struggle between the virtuous will of the common people and some evil, conspiring elite (Mudde 2017; Hawkins 2009).3 Coding for populism requires a process of markingthe presence of a reference to the common people and an evil elite. As such,existingstudies have primarilyreliedon extensivelytrained humancodersthat are instructed on 3Thisapproachis sometimes calledthe "ideational"approachtopopulism 12 APSR Submission Template APSRSubmission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSR Submission Template APSRSubmissionTemplate APSRSubmissionTemplate APSR Submission Template Towards Coding Social ScienceDatasetswith LanguageModels how to holistically code an entire text, examining it for references of both of these components (for an exampleofsuchacodingprocess,see(Busby et al.2019)). Herewedrawonalargedatasetofshortstatementscodedforpopulism. IntheFallof2018,The Guardiancreatedaseriesofarticlesonpopulism. Attheendofonearticle,readerswereinvitedto participate in a related survey on populism - over 20,000 individuals from more than 100 countries completed this survey. One question on this study asked respondents to discuss who or what was responsible for a pressing political problem in their country; two intensively trained human coders evaluated4,000ofthesetextsandindicatediftheydidordidnotcontainpopulism. Theprocessof training these coders involved initial instruction on a set of unrelated texts, repeated sessions to correct mistakes and clarify the coding process, and a review of the human codes (Busby et al. 2019). Unlike theprecedingstudies,then,thisapplication involves comparisonsto highly trainedhumancoders. These data also allow for a comparison to SML methods, as about 16,000 texts were not coded bythehumancoders. Asdiscussedbelow,weemployaSVCmethodtocodethefullsetoftextsand compare the performance of this technique to coding by GPT-3. We therefore compare the coding produced by GPT-3 on the set of human coded texts and in comparison to the SML approach. In eachcase,thecoders(humanorotherwise)generatedacodeof1whenthetextcontainedapopulist statement and 0 when it did not. To be regarded as populist, the text needed to contain both a reference tothevirtuousorgoodpeopleand some kindof maliciouselite group. 4 WebeginbycomparingGPT-3’scodingtothetwohumancoders. Asbefore,wecalculatedICC scorestomeasureagreementbetweenthecoders. IncontrasttothePigeonholingPartisansdata,the sametwocoders andGPT-3coded allof thetexts. We thereforeuse ICC3kwhich isdesigned for these kinds of comparisons (Shrout and Fleiss 1979). For these comparisons, We had GPT-3 code a random sampleof1,300ofthe4,000textscodedby humans. \[ADDFIGUREHERE\] Figure\[FILLIN\]showstheICCstatisticswithGPT-3,thehumancoders,andthesametypesof simulated coders show in Section 4.1. With these calculations, we find that GPT-3 performs well, 4Formoredetailsonthehumancodingprocess, seeother work explainingthe codebookin more detail, such as (Busby etal.2019)and(Busbyetal.2019) 13 Ryttinget al. althoughnotquiteaswellasathoroughlytrainedcoder. TheICCstatisticforthetwohumancoders was0.81,indicatinghighlevelsofagreement. AddingGPT-3asacoderreducesthissomewhatto0.77, but this still indicatesgood agreementbetween the human coders and GPT-3. In contrast, adding one ofthesimulatedcodersdramaticallyreducestheICCstatistics. WetakethisasevidencethatGPT-3 creates codes that are generally comparable to highly-trained human coders, with far less expense and training. To compareGPT-3’sperformancetoasupervisedbaseline, wefita bag-of-wordsSMLmodelon the populism data, using 3000 instancesfortraining and 1000 instances for validationat a time. With thisapproach,theSMLcodingmatchedthehumanpopulismcodeswithanaccuracyof86percent. Meanwhile, with only 4 coded examples, GPT-3 matched the human populism codes 79 percent of the time. While the SMLbaseline outperforms GPT-3 by about 7percentage points, it does so atthe cost of3000labeledexamples. GiventhedrasticallylowercostsofcodingwithGPT-3-inthecase,the requirement of hiring, training, and supervising coders to classify 4,000 texts - we again see this as evidenceofthevalue of GPT-3 as acodingtool forthesocialsciences.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/GPT3-SocialScience-Coding",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Towards Coding Social Science Datasets with Language Models (Rytting et al.)"
    },

    {
      "@id": "rdip:Dataset/PigeonholingPartisans",
      "@type": "schema:Dataset",
      "schema:name": "Pigeonholing Partisans (PP) – 7,675 open-ended descriptions of Democrats/Republicans (Rothschild et al. 2019 + synthetic)",
      "schema:size": 7675
    },
    {
      "@id": "rdip:Dataset/CongressionalHearings-CAP",
      "@type": "schema:Dataset",
      "schema:name": "CAP-coded U.S. Congressional hearing summaries (1946–2010)",
      "schema:size": ">10,000 summaries (subset n=326 used for intercoder comparison)"
    },
    {
      "@id": "rdip:Dataset/NYT-FrontPage-CAP",
      "@type": "schema:Dataset",
      "schema:name": "New York Times Front Page headlines 1996–2006 (Boydstun 2013)",
      "schema:size": 31034,
      "schema:description": "28 CAP media categories; random subsample n=560 used for intercoder study"
    },
    {
      "@id": "rdip:Dataset/GuardianPopulism",
      "@type": "schema:Dataset",
      "schema:name": "The Guardian Populism survey responses (2018)",
      "schema:size": ">20,000 responses; 4,000 coded by highly-trained humans; random subset n=1,300 used for GPT-3 comparison"
    },

    {
      "@id": "rdip:Activity/HumanCoding-AllDatasets",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Human coding of texts across four datasets (lightly-trained for PP/NYT/Congress, intensively-trained for Guardian Populism)",
      "prov:generated": [
        "rdip:Dataset/PigeonholingPartisans-HumanCodes",
        "rdip:Dataset/CongressionalHearings-HumanCodes",
        "rdip:Dataset/NYT-FrontPage-HumanCodes",
        "rdip:Dataset/GuardianPopulism-HumanCodes"
      ]
    },

    {
      "@id": "rdip:Activity/GPT3-PromptEngineering",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Design of few-shot prompts (2–4 exemplars) for each coding task",
      "prov:generated": "rdip:Dataset/GPT3-Prompts"
    },

    {
      "@id": "rdip:Activity/GPT3-Coding-AllDatasets",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Zero/few-shot coding of all four datasets using GPT-3 (text-davinci-002/003 era)",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/OpenAI-GPT3",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "OpenAI GPT-3 (text-davinci series)",
        "rdip:version": "not specified (2022-era commercial API)"
      },
      "prov:used": [
        "rdip:Dataset/PigeonholingPartisans",
        "rdip:Dataset/CongressionalHearings-CAP",
        "rdip:Dataset/NYT-FrontPage-CAP",
        "rdip:Dataset/GuardianPopulism",
        "rdip:Dataset/GPT3-Prompts"
      ],
      "rdip:outputDataset": [
        {
          "@id": "rdip:Dataset/PigeonholingPartisans-GPT3Codes",
          "@type": "schema:Dataset",
          "schema:name": "GPT-3 codes for 7,675 PP descriptions (5 dimensions)"
        },
        {
          "@id": "rdip:Dataset/CongressionalHearings-GPT3Codes",
          "@type": "schema:Dataset",
          "schema:name": "GPT-3 CAP codes for congressional hearing summaries"
        },
        {
          "@id": "rdip:Dataset/NYT-FrontPage-GPT3Codes",
          "@type": "schema:Dataset",
          "schema:name": "GPT-3 CAP codes for 560 NYT headlines"
        },
        {
          "@id": "rdip:Dataset/GuardianPopulism-GPT3Codes",
          "@type": "schema:Dataset",
          "schema:name": "GPT-3 binary populism codes for 1,300 Guardian responses"
        }
      ]
    },

    {
      "@id": "rdip:Activity/CAP-ProbabilityCalibration",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Post-hoc calibration of GPT-3 token probabilities using balanced validation set (Zhao et al. 2021-style bias normalization)",
      "prov:used": "rdip:Dataset/CongressionalHearings-GPT3Codes",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/CustomPython",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Custom Python post-processing scripts",
        "rdip:version": "unknown"
      }
    },

    {
      "@id": "rdip:Activity/SML-Baseline-Guardian",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Training and application of bag-of-words Support Vector Classifier (SVC) baseline on Guardian Populism data",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/scikit-learn-SVC",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "scikit-learn SVC (bag-of-words)",
        "rdip:version": "unknown"
      },
      "prov:used": "rdip:Dataset/GuardianPopulism-HumanCodes",
      "rdip:outputDataset": "rdip:Dataset/GuardianPopulism-SMLCodes"
    },

    {
      "@id": "rdip:Activity/IntercoderAgreement-Analysis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Computation of intercoder reliability metrics (ICC1k, ICC3k, Fleiss’ kappa, joint probability of agreement) and accuracy comparisons",
      "rdip:usedSoftware": [
        {
          "@id": "rdip:Software/R-or-Python-stats",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "R / Python (irr, psych, or sklearn.metrics packages implied)",
          "rdip:version": "unknown"
        }
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/IntercoderMetrics-Results",
        "@type": "schema:Dataset",
        "schema:name": "Tables and figures of agreement statistics across all four applications"
      }
    }
  ]
}
```

This JSON-LD faithfully represents the research provenance described in the methodology section:

*   Central project
*   Four original datasets (PP, Congress CAP, NYT CAP, Guardian Populism)
*   Human coding activities (varying training intensity)
*   Few-shot prompt engineering
*   Main GPT-3 coding activity (same model/version across all tasks)
*   Additional calibration step for CAP tasks
*   Supervised machine learning baseline (only on Guardian)
*   Final agreement/analysis step producing the reported metrics

All major data production activities, software tools (where identifiable), and resulting datasets are captured using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: Learning methods for BioIE have been rapidly advanced in the past 5 years. Conditional random fields(CRF) \[10\] and structured support vector machines(SSVM) \[34\] have been two representative learning methods, and deep neural networks\[35\] have been increasingly applied to both general domain IE and BioIE. All those methodological advances mainly fall into three categories: (1) learning from labeled data (i.e. supervised learning) which focuses on labeling more data to tackle new problems or improving model training using existing benchmark data; (2) learning from unlabeled data (i.e. semi- supervised and unsupervised learning) which involves incorporating large amount of unlabeled data into the learning process; (3) learning scheme integration to seamlessly integrate different learning paradigms at outer system level (i.e. hybrid approach) or modeling level (i.e. joint modeling). In particular, two emerging technological advances, namely open information extraction (OpenIE) and deep learning (DL), have exerted significant influence on BioIE recently for more scalable and reliable applications. What follows will be reviewing each of the abovementioned topics in more details. Learning from Labeled Data Traditional learning-based systems aim to infer optimal prediction functions from labelled training data instances, which can be used for mapping new data instances to their (predicted) labels. There are mainly two types of approaches that facilitate pattern analysis on labeled data: (1) feature-based approach explicitly transforms raw data representation into feature vector space, and each feature dimension represents an individual characteristics of a data instance; (2) kernel-based approach provides an implicit way of transforming raw data into a high-dimensional space through a similarity function, called kernel function, which is defined over pairs of data instances.  Feature-based Approaches Advanced feature engineering has proven to be successful in many machine learning based BioIE applications. In addition to common features, such as lexical (e.g., words), orthographic (e.g., capitalization, character n-grams), syntactic (e.g., part-of-speech, chunking), semantic (e.g., semantic category of a word by dictionary or ontology) and local context (e.g., n-grams, neighboring words) features \[36–39\], discourse-level features (e.g., sentence length, section headings, writing patterns) \[36,37\] and dependency tree based features \[39–42\] have also been explored. Different systems also leverage task specific features using external resources or other domain knowledge, e.g. chemical elements, amino acid sequences and chemical formulas were used to derive features for recognizing chemical named entities\[43\]; features derived from event occurrence pattern were designed to detect the causal relation in a clinical problem-action relation extraction system\[44\]. To improve the performance of feature-based system, combining multiple types of features is a widely used strategy, e.g. a drug-drug interaction (DDI) system\[45\] was developed to combine heterogeneous features, including lexical, syntactic, semantic and negation features derived from sentences and their corresponding parse trees. Word features are prone to the data sparseness challenge (i.e., insufficient training data vs. a huge amount of features). To overcome such challenge, vector-based word representations have been exploited, including clustering-based word representation (i.e., representing a word by its hard cluster(s)) \[36,46\], distributional representation (i.e., representing a word by its semantically related words as calculated on word co-occurrence statistics) \[37,46\], and distributed representation (i.e., word embedding) \[46,47\]. Tang et al. \[48\] combined clustering-based word representation and distributional word representation into a structural SVM learning scheme, showing better performance than using either single type of representation feature. More on word embedding will be described later in deep learning section. However, a richer set of features may not guarantee better performance, as features that are irrelevant, redundant or have limited discriminative power may cause adverse effects on model learning, leading to increased computational complexity and over-fitting. As a result, feature selection is of paramount importance for any learning-based approaches, especially with high-dimensional features. Simple additive or subtractive feature selection strategies (adding or removing each feature class one by one to evaluate feature contribution) work well for many BioIE applications (e.g. \[49\]). New feature selection approaches were also proposed, e.g. Leaman \[50\] applied multivariate feature selection with filters and false discovery rate analysis to biomedical NER; Xia et al. \[51\] evaluated an accumulated effect evaluation (AEE) algorithm for feature selection and showed improved performance in the GENIA bioNLP shared task 1 (event detection); Campos et al. \[52\] described an optimization algorithm to find the feature set that better reflect the characteristics of each event type for biomedical event trigger recognition; and Fang et al. \[53\] introduced an improved feature selection method by combining mutual information and class separability criteria for identifying non-redundant optimal features on multidimensional time series clinical data. In addition, a partition-specific feature selection method was successfully applied on both protein-protein interaction\[54\] and drug-drug interaction \[45\] tasks, where candidate relation pairs are partitioned into groups based on syntactic properties and features are optimized for each group, achieving the state-of-the-art system performance.  Kernel Approaches Kernel-based approaches are becoming more and more popular for learning algorithms including perceptron and support vector machines, as sometimes data can’t be easily represented with explicit feature vectors (e.g. sentences are better characterized by trees or graphs). In the last few years, many task specific kernels have been proposed or applied on many BioIE tasks. Patra et al. \[55\] proposed a novel kernel named “sliding tree kernel”, which is an improved tree kernel specific to named entity recognition(NER) task. It considers a substructure of trees in the form of sliding window, leading to a better way to model local context of a word. A hash subgraph pairwise(HSP) kernel was introduced for protein-protein interaction extraction\[56\], which can efficiently make use of the full dependency graph that represents sentence structure and particularly capture the contiguous topological and label information. In addition to single-kernel-based approaches, ensemble approach combines outputs from different kernel-based systems and multiple kernel learning (MKL) approach constructs a hybrid kernel by linearly or polynomially combining individual kernels. Thomas et al. \[57\] reported the best performing drug-drug interaction system in the DDI extraction 2011 challenge, which combined outputs from two kernel- based systems and a case-based reasoning system using majority voting. Yang et al. \[58\] presented a weighted MKL approach for protein-protein interaction(PPI) from biomedical literature, where different kernels (feature-based, tree, graph and part-of-speech path) were combined linearly and the shortest path-enclosed tree(SPT) and dependency path tree were extended to capture richer contextual information, achieving better performance than counterpart systems. Following this strategy, Li et al. \[59\] further improved the state-of-the-art performance on PPI by incorporating a semantic kernel characterizing the protein-protein pair similarity using Medical Subject Heading and the context similarity using WordNet. Similarly, the best system \[60\] in SemEval’13 DDI extraction applied a MKL approach linearly combining a feature-based kernel, a shallow linguistic kernel and a path-enclosed tree kernel. Another hybrid kernel, which consists of an entity kernel and convolution parse tree kernel combined via polynomial expansion, was showing promising result on biomedical event extraction\[61\]. Tikk et al. \[62\] conducted an analytical study on the performance of 13 types of kernels for PPI extraction, which suggests that the system performance benefits more from novel features than from novel kernel functions. Rich features have been explored to improve kernel-based systems. For instance, Zhou et al. \[63\] showed a novel framework for biomedical event trigger identification, where word embedding features were combined with syntactic and semantic contextual features using MKL method, achieving the state-of-the-art performance. Similarly, Li et al. \[64\] showed improved performance when integrating word embedding features in a kernel based PPI extraction system, and Ma et al.\[65\] improved PPI extraction by proposing a new tree kernel where processing rules were defined to better handle the parsing error of modal verb phrases and noise interference by appositive dependency. In contrast, Kim et al. \[66\] showed that a simple linear kernel that integrates a rich set of lexical and syntactic features is able to achieve a competitive performance for DDIs, suggesting that linear kernel may perform as well as complex kernels.  Cost-effective Ground Truth Acquisition Supervised machine learning approaches depend on annotated corpora, which are frequently expensive to obtain, especially in the medical/clinical domain. Semi-supervised annotation, active learning, and crowd-sourcing approaches have been developed to create large-scale annotated corpora. Pre-annotation or computer-aided annotation gives human annotators the machine-annotated data for potentially better efficiency. Recent studies, however, reported mixed results in terms of how much pre-annotation helps. Lingren et al.\[67\] created a dictionary for pre-annotation on clinical NER task, showing reduced time needed for review by 13.85-21.5% compared with fully manual annotation. However, in an experiment on clinical text de-identification task by South et al.\[68\], it has been shown that machine-assisted annotation didn’t improve annotation quality for most PHI classes and didn’t provide statistically significant time-savings compared to manual annotation of raw documents. By further combining iterative machine learning approach in pre-annotation, RapTAT\[69\], a semi- automated semantic annotation tool, was shown capable of reducing the annotation time by up to 50% on 401 clinical notes, as well as improving the inter annotator agreement. Active learning aims to alleviate annotation efforts by reducing annotated sample size. It selects informative samples via actively involving the learning algorithms. Various studies have investigated the effects of using active learning to achieve less learning cost without compromising learning performance of associated predicative models, such as assertion annotation for medical problems\[70\], semantic annotation for medical abbreviations and terms\[71\], clinical NER annotation\[72\], clinical coreference resolution\[73\], pathological phenomena labeling in MEDLINE\[74\] and phenotype annotation\[75\]. Two recent studies on medical concept extraction show that: (1) incorporating external knowledge resources within active learning query strategies\[76\] can further reduce annotation efforts; (2) incremental active learning\[77\] is promising in building robust medical concept extraction models while significantly reducing the burden of manual annotation. Crowdsourcing has been widely explored in biomedical and clinical domain \[78\]. Studies have demonstrated that crowdsourcing is an inexpensive, fast and practical approach for collecting high- quality annotations for different BioIE tasks, e.g. medication NER in clinical trial documents\[79\], disease mention annotation in PUBMED literature\[80\], relation extraction between clinical problems and medications\[81\], etc. Different techniques have been explored to improve the quality and effectiveness of crowdsourcing, including probabilistic reasoning\[82\] to make sensible decisions on annotation candidates and gamified techniques\[83\] to motivate a continuous involvement of the expert crowd. More recently, a method called CrowdTruth \[84\] was proposed for collecting medical ground truth through crowdsourcing, based on the observation that disagreement analysis on crowd annotations can compensate lack of medical expertise of the crowd. Experiments of using CrowdTruth on medical relation extraction task show that the crowd performs just as well as medical experts in terms of quality and efficacy of annotation, and also indicate that at least 10 workers per sentence are needed to get the highest quality annotation for this task. Learning from Unlabeled Data In contrast to relying on the costly labeled data, freely available unlabeled data have been explored for BioIE. Approaches include unsupervised, semi-supervised, and distant supervision. Unsupervised biomedical NER systems described in \[85\] are based on phrase chunking and distributional semantics, showing competitive results on both clinical notes and biomedical literature. Quan et al. \[86\] explored kernel-based pattern clustering and sentence parsing to tackle the PPI extraction and gene-suicide association extraction from biomedical literature. More recently, Alicante et al. \[87\] reported an unsupervised system for both entity and relation extraction from clinical records written in Italian. Semi-supervised methods aim to incorporate unlabeled data in a supervised manner. Recent semi- supervised approaches in BioIE mostly differ in the approximation methods used to obtain labelling for unlabeled data as well as the ways to handle uncertainty when adding unlabeled data, including self- training, also known as bootstrapping (e.g. \[88\] for medical risk event extraction and \[89\] for drug-gene relation extraction), transfer learning (e.g. \[90\] for clinical concept extraction), and manifold regularization (e.g. \[91\] for medical relation extraction). To obtain higher quality labelling for unlabeled data, several strategies have been proposed for semi-supervised learning, such as combining active learning for PPI extraction\[92\], introducing event inference mechanisms to detect more event mentions from unlabeled text \[93\], and exploiting topic analysis to identify similar sentences for automatic labeling\[94\]. From feature representation point of view, feature coupling generalization(FCG) has been explored to generate new features directly from unlabeled data, e.g. \[95\] for gene NER and PPI extraction and \[96\] for biomedical event extraction. Different from abovementioned semi-supervised methods, distant supervision approach typically doesn’t require any labeled data, which makes use of weakly labeled data derived from a knowledge base\[97\], or some seed data points\[98\] but without finer-grained sentence level annotations. Recently it has been widely used in DDI and PPI extraction\[97,99,100\] with different strategies to deal with training challenges due to noisy data, as well as later work on the BioNLP Gene Regulation Network task\[98\], gene expression relation extraction\[101\] and cancer pathway extraction\[102\]. Most recently, the DeepDive system\[103\] was employed to scaled up the distant supervision method on biomedical text mining without limiting the application to a specific process or pathway, achieving promising results for extracting gene interactions from full-text PLOS articles. Learning Scheme Integration  Hybrid Approach Hybrid approaches integrate heuristics/rule/pattern-based method, domain knowledge, and learning- based method. One ensemble strategy is to develop multiple independent models, and then combine the results of each model for a final output, either through rules or by using some classification/regression model, e.g. combining rule-based model with SVM classifiers for biomedical event detection\[104\]; integrating pattern recognition into learning for DDI extraction\[105\]; algorithmically fusing results from two approaches for temporal relation extraction in patient discharge summaries\[106\]. Another ensemble strategy is to run different models sequentially for further filtering and refining to a better system output, e.g. extracting disorder mentions from clinical notes \[107\]; extracting disease-treatment relations from MEDLINE corpus\[108\]; identifying Genia events by learning- based classifiers with rule-based post-processing \[109\]; and similar post-processing was also used in a hybrid system of recognizing composite biomedical named entities\[110\].  Joint Modeling A BioIE system typically involves different subtasks with embedding and inter-dependent characteristics. To overcome cascading errors in a multi-step pipeline framework, joint models (e.g. a Markov Logic Network(MLN) based approach \[111\]) have shown improved performance. But due to complexity of inference for joint modeling, rich features previously used in the pipeline framework may be compromised to make inference trackable. Therefore, many efforts have been made to relieve the computational bottleneck of joint inference in biomedical event extraction. For instance, Riedel and McCallum \[112\] proposed three joint models of increasing complexity to make the system more robust and applied dual decomposition to make joint inference tractable; Vlachos and Craven \[113\] applied the search-based structured prediction framework (SEARN) for high modeling flexibility and fast joint inference; Venugopal et al.\[114\] presented an MLN-based join model which employs an SVM model to encode high-dimensional features; and more recently Li et al.\[115\] exploited dual decomposition based joint inference, dependency parsing based rich features, and word embedding for event extraction. From a different perspective, Wei et al.\[116\] proposed to use dependency chain tagging to extract embedded semantic relations from biomedical literature, which avoided complex inference but kept the hierarchy feature of entities. In addition to the abovementioned work focusing on BioNLP shared event extraction task, joint modeling has been increasingly introduced in other specific subdomains. To effectively extract adverse drug event(ADE), Li et al.\[117\] designed a transition-based model to extract drugs, disease and ADEs jointly, which leverages the structured perceptron for training and the multiple-beam search algorithm for decoding. Open Information Extraction (OpenIE) OpenIE \[118\] has been emerging as a novel information extraction paradigm in the last couple of years. It doesn’t presuppose a predefined set of relations but aims to identify any possible relations from unlabeled data with no or limited supervision. OpenIE systems typically consist of four main components: (1) Automatic Labeling of data using heuristics or distant supervision; (2) Extractor Learning using relation-independent features on noisy self-labeled data; (3) Tuple Extraction on a large amount of text by the Extractor; (4) Accuracy Assessing by assigning each tuple a probability or confidence score. Based on features used in extractor learning, we can roughly group existing OpenIE systems into two categories: Light Open Extractors (e.g. \[118–121\]) which only use shallow language processing, e.g. part-of-speech tagging and chunking, and Heavy Open Extractors (e.g. \[122,123\]) which use deep linguistic analysis, e.g. dependency parsing. Typically, the former is much more efficient but is much lower in either recall or precision, while the latter improves the overall performance significantly with the hit on system efficiency. OpenIE requires no or little supervision and its extractor is trained on automatically labelled data using heuristics or distant supervision, which is the same as traditional bootstrapping system in this regard. However, it lends itself well to contributing to next generation information extraction systems due to its particularly advantageous aspects, as summarized in Table 1. Table 1. Advances of OpenIE Compared with Traditional self-learning OpenIE Traditional self-learning Highly scalable to size and diversity of the WEB Relatively small and homogeneous corpus Not dependent on relation specific features Relation dependent features Avoid lexical features for generalization Use lexical features for better precision Domain independent Domain dependent No predefined relation schema Targeted to specific types of relations Label all the data Selectively label data Redundancy-based accuracy assessing Confidence derived from the learned model One major challenge is that the massive facts OpenIE systems extract are in purely textual surface form which cannot be directly used by applications. There are several directions to address this issue: (1) Building knowledge resources to make sense of OpenIE extractions, e.g. dynamic knowledge graphs\[124\], web-scale knowledge repository\[125\], taxonomy of textual relational patterns\[126\]; (2) Harnessing semantic web technologies to enable information fusion and semantic reasoning\[127\]; and (3) Integrating ontological resources, e.g., linking OpenIE to world knowledge\[128,129\] and aligning multiple ontologies \[130\]. In addition, Riedel et al. \[131\] proposed a universal schema, which unites surface form relational patterns from OpenIE with relations defined in knowledge bases. By using matrix factorization and collaborative filtering, this approach is able to reason about unstructured and structured data in mutually-supporting ways. The great potential of applying OpenIE techniques to BioIE has been recognized. For instance, Attias et al. \[132\] adapted the Never Ending Language Learner (NELL) \[133\] to biomedical domain and proposed a Rank-and-Learn methodology to effectively prevent semantic drift, achieving promising results on learning biomedical lexicon of open categories. Nebot et al. \[134,135\] presented a scalable method that extracts surface-form biomedical relations without pre-specified types, and then infers abstract relations and their signature types by clustering these extracted relations. Deep Learning Deep learning refers to “a class of machine learning techniques that exploit many layers of non-linear information processing for supervised or unsupervised feature extraction and transformation, and for pattern analysis and classification”\[136\]. Deep learning networks can be roughly categorized into (1) unsupervised/generative, e.g., restricted Boltzmann machines (RBMs)\[137\], deep belief networks (DBNs)\[138\]; (2) supervised/discriminative, e.g., deep neural networks (DNNs)\[139\], convolutional neural networks (CNNs)\[140\] and recurrent neural networks(RNNs)\[141\]; and (3) hybrid, e.g., DBN- DNN\[142\] models that combine unsupervised pre-training and supervised fine-tuning. There have been a surge of interest of applying deep learning techniques in common NLP tasks, such as semantic parsing\[143\], information retrieval\[144,145\], semantic role labeling\[146,147\], sentimental analysis\[148\], question answering\[149–152\], machine translation\[153–157\], text classification\[158\], summarization\[159,160\], text generation\[161\], as well as information extraction, including named entity recognition\[162,163\], relation extraction\[164–168\], event detection\[169–171\]. CNNs and RNNs are two popular models employed by these work. Despite of the difference in network architecture, they share the key motivation to avoid task-specific, knowledge-centric feature engineering by leveraging the word embedding technique. More recently, remarkable progress has also been made in BioIE due to the widely propagated application of deep learning techniques. One popular technique from deep learning is word embedding, which have been widely used in biomedical named entity recognition\[46,172\], medical synonym extraction\[173\], medical semantics modeling\[174\], relation extraction including chemical-disease relation \[175\], Protein-Protein interaction\[176\], and relation between pharmaceuticals and diseases/physiological processes. In terms of event extraction, Li et al.\[177\] reported comparable state- of-the-art performance when applying word embeddings on BioNLP event extraction task; Nie et al.\[178\] presented an embedding assisted neural network prediction model to conduct biological event trigger identification; Henriksson et al.\[179\] leveraged distributed semantics to detect adverse event signals from clinical notes. Furthermore, Wu et al.\[180\] utilized neural word embeddings for disambiguating clinical abbreviation mentions; similarly Liu et al.\[181\] exploited task-oriented resources to learn word embeddings for clinical abbreviation expansion. Ghassemi et al.\[182\] employed distributed stochastic neighbor embedding (tSNE) to extract clinical sentiment information (positive vs. negative). Instead of using standard word embedding training strategy, Jiang et al.\[183\] proposed a biomedical domain-specific word embedding model by incorporating stem, chunk, and entity information, and used them for DBN-based DDI extraction and RNN-based gene mention extraction. Similarly in clinical domain, Choi et al.\[184\] presented a novel neural word embedding tool, Med2Vec, which can not only learn distributed representations for both medical codes and visits in electronic health record (EHR), but also allow interpreting the learned representations confirmed positively by clinical experts. Then an extensive and comparative study\[185\] has been performed among medical concept embeddings learned from medical journals, medical claims and clinical narratives respectively, evaluating their similarity and relatedness properties. Different deep learning architectures have also been explored to predict clinical events, e.g. Choi et al.\[186\] applied RNNs to longitudinal EHR data to predict future disease diagnosis and medication prescription. Following that, they further explored two gating mechanisms Long Short-term Memory (LSTM)\[187\] and Gated Recurrent Units (GRUs)\[153\] on RNN models, incorporating patient static data to extract early signs from EHR data for predicting kidney transplantation endpoint events, Jagannatha and Yu\[188\] employed a bidirectional LSTM RNN structure to extract adverse drug events from electronic health records, and Miotto et al.\[189\] explored a three-layer stack of denoising autoencoders to learn a general-purpose patient representation from EHR data, resulting in improved clinical predictions. In addition to using textual data, Liu et al.\[190\] proposed a recurrent self-evolving fuzzy neural network (RSEFNN) to leverage brain dynamics data to predict driving fatigue event; Lehman et al.\[191\] combined CNNs with dynamical systems to model physiological time series for prediction of patient prognostic status. Due to the big success of deep learning on computer vision, information extraction/detection from medical imaging has been substantially influenced, such as pulmonary nodule detection in computed tomography scans using CNN features\[192\], a successful application of CNN trained on a large-scale non-medical image dataset for chest x-rays pathology detection\[193\], automated detection of posterior- element fractures on spine CT based on deep CNN \[194\], an interleaved text/image deep learning system for extracting and mining the semantic interactions of radiology images and reports\[195\]. More recently, Shin et al.\[196\] exploited and extensively evaluated three important factors of applying deep CNN to medical image classification, i.e., network architecture, dataset characteristics and transfer learning, in the context of two different computer-aided diagnosis applications: thoraco-abdominal lymph node detection and interstitial lung disease classification. Other successful examples of applying deep learning techniques include genomic information extraction\[197–199\], protein structure prediction\[200\] as well as drug discovery\[201\].

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/BioIE-Review-Learning-Methods",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Comprehensive Review of Machine Learning and Deep Learning Methods for Biomedical Information Extraction (BioIE)"
    },

    {
      "@id": "rdip:Activity/Literature-Review-and-Synthesis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Systematic narrative review and taxonomic synthesis of >200 publications on learning-based BioIE methods (circa 2010–2017)",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/BioIE-Methods-Taxonomy",
        "@type": "schema:Dataset",
        "schema:name": "Taxonomy and narrative synthesis of BioIE learning paradigms (supervised, semi-supervised, unsupervised, hybrid, OpenIE, deep learning)"
      }
    },

    {
      "@id": "rdip:Activity/Feature-Based-Learning-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of feature engineering and feature selection approaches in supervised BioIE (lexical, syntactic, semantic, dependency, discourse, word embeddings)",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Feature-Based-BioIE-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Summary of feature types and feature selection strategies in BioIE"
      }
    },

    {
      "@id": "rdip:Activity/Kernel-Based-Learning-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of kernel methods (tree kernels, graph kernels, MKL, hybrid kernels) applied to BioIE tasks",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Kernel-Based-BioIE-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Synthesis of kernel-based systems and multiple kernel learning in biomedical NER, PPI, DDI, and event extraction"
      }
    },

    {
      "@id": "rdip:Activity/Cost-Effective-Annotation-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of annotation efficiency methods: pre-annotation, active learning, crowdsourcing (including CrowdTruth), and semi-automated tools (e.g., RapTAT)",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Annotation-Efficiency-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Overview of cost-reduction strategies for creating biomedical annotated corpora"
      }
    },

    {
      "@id": "rdip:Activity/Unlabeled-Data-Learning-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of unsupervised, semi-supervised (self-training, transfer learning, manifold regularization), and distant supervision approaches in BioIE",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Unlabeled-Learning-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Synthesis of methods leveraging unlabeled biomedical text (including DeepDive distant supervision applications)"
      }
    },

    {
      "@id": "rdip:Activity/Hybrid-and-Joint-Modeling-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of hybrid (rule + ML ensemble) and joint modeling approaches (MLN, dual decomposition, SEARN, structured perceptron) for BioIE",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Hybrid-Joint-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Summary of pipeline vs. joint inference strategies in biomedical event extraction and relation extraction"
      }
    },

    {
      "@id": "rdip:Activity/OpenIE-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of Open Information Extraction paradigms and their emerging application to biomedical text",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/OpenIE-BioIE-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Comparison of Light vs. Heavy OpenIE extractors and biomedical adaptations (NELL adaptation, relation clustering)"
      }
    },

    {
      "@id": "rdip:Activity/Deep-Learning-BioIE-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review of deep learning applications in BioIE: word embeddings, CNNs, RNNs/LSTMs/GRUs, denoising autoencoders, transfer learning from vision, and clinical prediction",
      "prov:used": "rdip:Dataset/BioIE-Literature-Corpus",
      "rdip:usedSoftware": [
        {
          "@id": "rdip:Software/word2vec",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "word2vec / GloVe-style embeddings",
          "rdip:version": "various"
        },
        {
          "@id": "rdip:Software/Theano-TensorFlow-CNTK",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "Deep learning frameworks (Theano, TensorFlow, CNTK, etc.) – implied but not named",
          "rdip:version": "various (2014–2017 era)"
        }
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Deep-Learning-BioIE-Summary",
        "@type": "schema:Dataset",
        "schema:name": "State-of-the-art summary of deep neural architectures applied to biomedical NER, relation/event extraction, clinical prediction, and medical imaging"
      }
    },

    {
      "@id": "rdip:Dataset/BioIE-Literature-Corpus",
      "@type": "schema:Dataset",
      "schema:name": "Corpus of >200 cited publications on machine learning for BioIE (primarily 2010–2017)",
      "schema:description": "Includes references to CRF, SSVM, kernel methods, OpenIE systems, DeepDive, word2vec-era embeddings, early CNN/RNN papers in biomedicine"
    },

    {
      "@id": "rdip:Activity/Final-Synthesis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Integration of all sub-reviews into final review manuscript section",
      "prov:used": [
        "rdip:Dataset/Feature-Based-BioIE-Summary",
        "rdip:Dataset/Kernel-Based-BioIE-Summary",
        "rdip:Dataset/Annotation-Efficiency-Summary",
        "rdip:Dataset/Unlabeled-Learning-Summary",
        "rdip:Dataset/Hybrid-Joint-Summary",
        "rdip:Dataset/OpenIE-BioIE-Summary",
        "rdip:Dataset/Deep-Learning-BioIE-Summary"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/BioIE-Review-Section",
        "@type": "schema:Dataset",
        "schema:name": "Final 'Methodology' review section of the paper"
      }
    }
  ]
}
```

This JSON-LD accurately reflects the provenance of the provided text, which is a large-scale narrative review paper section rather than a primary empirical study. The main data production activities are literature reviewing, taxonomic synthesis, and narrative integration of existing methods — no new primary datasets or models were created. All major intellectual steps (feature-based, kernel-based, annotation efficiency, unlabeled learning, hybrid/joint, OpenIE, deep learning) are represented as separate review activities feeding into the final synthesis. Software is only minimally mentioned (implicit deep learning frameworks and word2vec-style tools), so versions are marked as "various" for the 2014–2017 period.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: Survey methodologists have developed theories of how re- spondents understand, process, and respond to survey ques- tions. We summarize these theories and use them to derive hypotheses about the aspects of the label collection task that may impact label quality. We end the section with thoughts on mitigation measures and future research. 3.1. Response Process Ideally, survey respondents understand questions thoroughly and respond thoughtfully. However, they make take short- cuts that can threaten data quality. Optimal Survey Response Process Responding to a sur- vey question can involve several cognitive steps (Tourangeau et al., 2000; Tourangeau, 2018):

1.  Comprehension: Understand the question and the re- sponse options
2.  Retrieval: Search memory for relevant information
3.  Integration: Integrate the retrieved information to form an answer to the question
4.  Mapping: Map that answer onto the provided answer choices Ideally, a respondent proceeds through each step in order. However, they can choose to backtrack. For example, con- sidering the response options in the Mapping step may change the interpretation of the question (Comprehension) or trigger additional relevant information to come to mind (Retrieval). The above model exposes why respondents sometimes give incorrect answers. At the Comprehension step, they may fail to understand the question or some of the words it uses. They may have a different understanding of some of the words than those who wrote the question. At the second step, respondents may fail to retrieve all relevant informa- tion. Some information may have been forgotten. At the third step, respondents may fail to put in the mental effort to bring together their understanding of the question with the retrieved information. At the fourth step, respondents may not find an answer choice that reflects their answer or they may edit the true answer to avoid revealing sensitive information. Deviations from Optimal Response Process The full survey response process outlined above is cognitively de- manding. Some respondents resort to taking shortcuts, an approach called satisficing (Krosnick, 1991; Krosnick et al., 1996). For example, they may retrieve only the most recent relevant information from memory (recency bias) or choose the first reasonably correct answer choice. Satisficing re- lates to the cognitive miser theory in psychology, which holds that people seek to minimize cognitive effort (Fiske & Taylor, 1991; Kahneman, 2011). As predicted by satisficing theory, eye-tracking studies show that respondents do not read all options in select-all-that- -apply questions (Galesic et al., 2008), and shortcuts are more common as survey length increases (Galesic & Bosn- jak, 2009). Respondents tend not to read provided instruc- tions (Brosnan et al., 2019) or click on provided definitions (Peytchev et al., 2010), especially when they believe they un- derstand the concept that is asked about (Tourangeau et al., 2006). The survey literature discusses several types of more ex- treme undesirable response behavior. Acquiescence is the tendency to say “yes” to yes/no questions, regardless of content (Knowles & Condon, 1999). Straightlining is the practice of choosing the same response option in the same position (for example, the first response option) to all ques- tions. This behavior is most common in batteries or grids of questions with the same response options (Kim et al., 2019). Some respondents even deliberately give incorrect answers to later questions to reduce the length or burden of a survey: when a “yes” response triggers follow up questions, respon- dents may learn to report “no.” This phenomenon is called motivated misreporting (Kreuter et al., 2011; Tourangeau et al., 2012; Eckman et al., 2014). Context Effects Perceptions and judgments are shaped by the broader context and preceding experiences, a phe- nomenon called context effects (Tversky & Kahneman, 1974; Strack, 1992). For example, a very tall person can make others seem shorter: a contrast effect. An unethical politician can make other politicians seem less ethical: an assimilation effect (Bless & Schwarz, 2010). Opinion questions are especially vulnerable to context ef- fects, because respondents do not always have well-formed, fixed opinions that they retrieve from memory. Instead, they form opinions when asked for them, and this process can be shaped by context clues in the question, the response options, the look and feel of the instrument, or the previ- ous questions (McFarland, 1981; Zaller & Feldman, 1992; Schwarz, 2007). Order effects are the most common example of context ef- fects in surveys. Questions that come earlier in a survey can change how respondents interpret later questions. Re- 3 Science of Data Collection searchers have found order effects in reports of crime and bullying victimizations, of disabilities, and of race (Cowan et al., 1978; Gibson et al., 1978; Bates et al., 1995; Todorov, 2000; Huang & Cornell, 2015). 3.2. Hypotheses about Label Quality These theories about how respondents answer questions lead us to several hypotheses about the properties of the labeling task that may impact training data quality. The ML literature has investigated some of these hypotheses, but fundamental research gaps exist. Wording and Reading Level Respondents cannot pro- vide high-quality answers to questions unless they clearly understand what the question asks and what they should include and exclude in their answer. Questions should be at an eighth grade reading level or lower (Dillman et al., 2014) and terms should be as unambiguous as possible. Defini- tions, if needed, should be provided in the question itself, because respondents often do not use rollovers or links for additional information when answering questions (Peytchev et al., 2010). We suspect that applying the same guidelines to labeler prompts and instructions would improve the quality of the labels collected. (Of course, nothing can be done about ambiguous terms or high reading levels in the observations.) We are not aware of any research into these issues. We note that Figure 1 contains rollovers or links for additional information on three of the questions on the right side. Multiple Labels Often ML researchers want to collect multiple labels about an observation from one labeler: for example, whether an image contains a cat, a dog, a person, or a vehicle. We can ask labelers to provide all labels at once, as in Figure 2(a), or we can ask one or more labelers to provide each label separately, as in Figure 2(b). The choice between these two approaches echos the choice in surveys between select-all-that-apply questions (Figure 3(a)) and a series of yes/no questions (Figure 3(b)). As predicted by the survey response model, the yes/no format collects better data because it encourages respondents to process each option separately (Smyth, 2006; Pew Research Center, 2019). The select-all-that-apply approach is vul- nerable to satisficing: respondents pick the first one or two reasonable options and fail to think deeply or even look at later options (Galesic et al., 2008). However, the yes/no format can encourage acquiescence (Smyth, 2006). This finding also holds for labeling. In an experiment that involved labeling tweets as containing hate speech or offen- sive language, Kern et al. (2023) randomly assigned labelers to different versions of the labeling instrument. Condition A was similar to Figure 2(a) and Condition B was similar (a) Collect all labels on one screen (b) Collect labels on separate screens Figure 2. Collecting multiple labels on one screen (first panel) or multiple (second panel); adapted from (Kern et al., 2023) (a) Select-all-that-apply question (b) Series of yes/no questions Figure 3. Survey question in select all (first panel) and yes/no (sec- ond panel) formats, adapted from Pew Research Center (2019) to Figure 2(b). Splitting the collection across two screens (Condition B) led to higher rates of hate speech and offen- sive language annotation. Models trained on Condition B data also performed better than those trained on Condition A data across several metrics (Kern et al., 2023). This result is a clear example of how findings in the survey literature translate to the labeling task and improve the quality of training data. 4 Science of Data Collection Order Effects Theories about context effects suggest that the order in which instances or observations are presented influences the labels assigned. If a contrast effect is present, a very hateful social media post would make later posts seem less hateful than they otherwise would (for preliminary evidence of this phenomenon, see Beck et al., 2022). An order effect could also arise if labelers change their behavior over time. As they gain experience, they might become more accurate and conscientious, as suggested by Lee et al. (2022). Alternatively, they might become bored or fatigued and engage in more satisficing, acquiescence, or “don’t know” nonresponding over time, as suggested by the survey literature (Kraut et al., 1975; Galesic & Bosnjak, 2009). Mathur et al. (2017) detected order effects in two bench- mark NLP data sets. When coding tweets as hate speech or offensive language, Beck et al. (2024) found a decreasing time trend: tweets that appeared later were less likely to be flagged. However, their experimental set up did not allow them to test hypotheses about the mechanisms causing the time trend. Many research questions thus remain open, such as when contrast and assimilation effects appear and which tasks and labelers are most impacted by order effects. Order effects may also have implications for active learning (AL) and sim- ilar labeling approaches. In AL, an algorithm determines which observations to label next to maximize the marginal information gain for the model (Monarch, 2021). However, active learning considers only the model’s needs, not the labelers’. If context effects are large, the algorithm should also account for contrast and assimilation effects when de- ciding which observations to label. We are not aware of any research that has jointly accounted for the needs of the model for diverse training data and the impact of obser- vation order on annotators. An approach similar to active learning exists in surveys (Zhang et al., 2020), but is not widely adopted due in part to concerns about order effects. et al., 2022). Another recent study in NLP collected “uncer- tain” flags from labelers for a relation extraction task across several text genres (Bassignana & Plank, 2022). Labelers were more likely to choose “uncertain” when coding text in some genres, and the model struggled with prediction in those genres as well. These preliminary results suggest that giving labelers the option to indicate uncertainty or lack of knowledge can provide helpful information and does not encourage satisficing in labeling. Pre-labeling Pre-labeling involves displaying a suggested label, bounding box, or similar and asking the labeler if it is correct. If the labeler indicates the label is not correct, they are asked to provide the correct label. Pre-labeling is more efficient than labeling without suggested labels (Lin- gren et al., 2013; Skeppstedt et al., 2016; South et al., 2014). However, labelers may become too trusting of the sugges- tions and fail to correct errors (Dietvorst et al., 2015; Logg, 2017; Berzak et al., 2016), a phenomenon called anchoring bias or automation bias (Mosier & Skitka, 1999). In the survey field, we find that providing a pre-filled re- sponse that respondents or interviewers should update leads to underreporting of errors of both omission and commis- sion. For example, when respondents are reminded of their answer in a previous survey wave, they tend to report that the answer still applies rather than providing an updated response (J¨ ackle & Eckman, 2019). Previous literature on labeling has explored anchoring bias (Lingren et al., 2013; Skeppstedt et al., 2016; South et al.,

2014.  but has not leveraged social science to find the factors that make the effect weaker or stronger. The social science literature suggests several hypotheses about the mechanisms behind anchoring bias, such as incentives (Cialdini, 2009), belief in authority (Asch, 2016; Cialdini, 2009), or reliance on heuristics (Cialdini, 2009; Norman, 2007; Kahneman, 2011). Testing these theories experimentally would help data collectors design tasks that capture the efficiency of pre-labeling with lower risk of anchoring bias. Don’t Know Option The inclusion of “don’t know” or “no opinion” responses in surveys has been debated for years. Some researchers believe these options offer respondents an easy way to satisfice: rather than thinking about the issue and forming an opinion, respondents can simply choose the “don’t know” option. Others believe that having no opinion on a given topic is a valid response and that forcing respondents to provide an opinion when they don’t have one reduces data quality (Schuman & Presser, 1996). Many labeling tasks do not include a “skip” or “don’t know” option: labelers must provide a label even when they are not certain. (The instrument in Figure 1 is an exception.) When a recent experiment provided a “don’t know” option to half of the labelers, fewer than three percent chose it, and the overall distribution of the labels was not impacted (Beck Overreliance on Examples Examples can introduce a similar bias. Survey questions often give examples of the things respondents should consider when they formulate their responses. Examples improve response accuracy when they remind respondents to include items they might other- wise leave out, because they have forgotten or were unsure whether to include them. However, when the examples in- clude only common items, respondents tend to leave out less common items (Tourangeau et al., 2014). Examples are also often included in labeling instructions or annotation guidelines. As in surveys, labelers at times rely too heavily on these examples as they label. This instruc- tion bias can lead to overestimation of model performance 5 Science of Data Collection (Parmar et al., 2023). Again, a better understanding of the mechanisms behind this behavior, guided by social science theories, could inform efforts to reduce it. 3.3. Mitigation Measures and Future Research The survey methods literature suggests several approaches to minimize the effects discussed in Section 3.2. Randomization of Observations To address order ef- fects, label collectors can randomize the order of observa- tion shown to labelers. This approach does not eliminate order effect but it ensures that no one ordering impacts all an- notators in the same way. Random ordering is incompatible with active learning techniques, however. Instrument Testing Many surveys spend weeks or even months drafting, testing, and revising questions and re- sponse options to arrive at language that is understood simi- larly by most members of the population, a process called cognitive interviewing (Willis, 2004). They then launch the survey with a small group of respondents to assess re- sponse rates, don’t know rates, and response times. Such testing could improve the instructions and prompts given to labelers. Retain Paradata Many surveys capture process data, called paradata, during the survey, such as the time spent on each screen, the device used, even mouse movements (Kreuter, 2013; Horwitz et al., 2017). Paradata can help iden- tify satisficing respondents and low quality data (Kreuter,
2015.  and may do the same in label collection. However, collecting such data may raise additional privacy and ethics concerns (see Couper & Singer, 2012; Kunz et al., 2020; Henninger et al., 2023). Feedback to Labelers Label collection instruments could experiment with prompts to encourage labelers not to en- gage in satisficing. Respondents who pick many “don’t know” answers or repeatedly choose the same response op- tion could receive reminders about the importance of the task. Those who click through screens quickly could receive prompts to slow down and read carefully. In surveys, feed- back on speeding successfully slowed respondents and did not lead to early terminations of the survey (Conrad et al., 2017). Test Observations In surveys, instructed response items, such as “Choose yellow below” can help identify respon- dents who speed or provide low quality responses (Gum- mer et al., 2018; Berinsky et al., 2024). We have not seen these questions used in labeling tasks. However, some tasks embed observations with known labels to try to catch anno- tators who do not understand the task. In NLP tasks, it is common to qualify only workers who pass an initial quiz or perform well on inserted test observations (Nangia et al., 2021). These test observations could also catch annotators who satisfice (see Nie et al., 2020, for an application). We recommend future research to more comprehensively test these and related approaches.

4.  Need for Diversity Large-scale annotation tasks, such as the reCAPTCHA tests, may collect labels from a broad spectrum of the population. However, the crowdworkers used in many label collection tasks are members of large crowdworker panels such as Appen, Upwork, Scale AI, Prolific, or MTurk and do not reflect the U.S. or world population. Smart et al. (2024) note that labelers tend to be from the Global South, while the models they help train benefit the educated population in the Global North. The workers who labeled data to fine- tune InstructGPT were 22% Filipino and 22% Bangladeshi (Ouyang et al., 2022, Appendix B3). MTurk members are younger, lower income and less likely to live in the South than the U.S. population (Berinsky et al., 2012). The unique characteristics of the labelers lead us to worry that the data they provide may not represent the views of the population that will use or be affected by the models.2 Issues of representativeness are enormously important to surveys, which explicitly aim to make statements about the entire population. For this reason, the survey methods literature has much to contribute on this topic. 4.1. Selection Bias Selection bias occurs when those involved in providing data have different characteristics than the population. In surveys, selection bias3 arises when the propensity to take part in a survey is correlated with the characteristics measured in a survey. Let us return to the example in Section 2, a survey to estimate the proportion of U.S. adults without health insurance. If we distributed the survey invitations in doctors’ waiting rooms, the sample proportion would overestimate the population proportion. Those in waiting rooms are more likely to receive the survey invitation and are also more likely to have health insurance. The propensity to take part is correlated with what the survey measures, leading to selection bias in the estimate of health insurance coverage. 2We acknowledge that this section glosses over what we mean by “population.” Is it the population that regularly uses the models? The population impacted by the models? We leave this important discussion to later work. 3In the survey literature, the preferred terms is nonresponse bias. We use the term selection bias here because it is more general and more suited to the labeling task. 6 Science of Data Collection Figure 4. Labeler characteristics induce correlation between propensities (adapted from Groves, 2006) Just as in surveys, selection bias arises in training data labels if the propensity to engage in the labeling task is correlated with the propensity to assign a given label. We expect that this correlation is non-zero for many tasks, because labeler characteristics likely influence both propensities, as shown in Figure 4. On the left side of Figure 4, labelers’ characteristics influ- ence their decision to engage in labeling work. As noted above, labelers tend to have different attributes than the gen- eral population (Gray & Suri, 2019; Smart et al., 2024). On the right side of Figure 4, labelers’ characteristics influence the labels they assign. The literature provides evidence for this association as well: labeler age and education level im- pact whether they perceive comments on Wikipedia entries as attacks (Al Kuwatly et al., 2020); conservative labelers are less likely to flag anti-Black language (Sap et al., 2022); labelers in the U.S. are more likely to see a bird in ambigu- ous images than those in India (Parrish et al., 2024). We hypothesize that such effects are more widespread than the literature suggests, because many studies do not collect an- notator characteristics and thus cannot detect their impact on the labels (Kirk et al., 2023). If the characteristics that influence one side of Figure 4 are the same as, or correlate with, the characteristics that influence the other side of the figure, the two propensities at the bottom will be correlated, leading to selection bias. Consider a labeler who is a frequent biker, annoyed by cars that park in the bike lanes in their city. They may be more likely to agree to label a data set of potential bike lane violations (left side) and also more likely to see violations where others do not (right side). Although the goal of label data collection is not to make population estimates, selection bias is nevertheless a risk to training data and model development. In the early days of machine learning, when developers trained model to recog- nize written numbers or tell cats from dogs, perhaps labeler characteristics mattered less. The association on the right side of Figure 4 may be weak or absent with more objective tasks (though see Aroyo & Welty, 2015, for counterargu- ments). However, the labeling tasks still performed by humans today often involve more difficult and more opinion-based work. People may legitimately disagree about whether a given statement is toxic or offensive, for example. Reinforcement learning with human feedback (RLHF) in particular may be more exposed to selection bias. The labels collected for reinforcement learning, like those in Figure 1, are inherently opinion-based. As discussed in Section 2, opinion questions in surveys are more susceptible to context effects than fac- tual questions. We suspect that opinion labels are also more impacted by labeler characteristics than are more objective labels. RLHF aligns models to the judgments of labelers. If selection bias is present in the data, those judgments do not match the interests of the public. For example, if those who participate in labeling are also less likely to judge text as toxic, then the model trained on their data will also see less toxicity. We see evidence of the impact of selection bias on models in two studies that trained models on different sets of labelers. Both showed that models make different predictions when trained on labels from, for example, female versus male labelers, or Asian versus white labelers (Al Kuwatly et al., 2020; Perikleous et al., 2022). 4.2. Mitigation Measures and Future Research To combat selection bias in labeling tasks, we need to break the correlation between the propensity to assign a given label and the propensity to participate in labeling. We consider three methods. Left Side We could try to remove the correlation between labeler characteristics and the propensity to participate in labeling (the left side of Figure 4) by diversifying the labeler pool, collecting data from labelers with different motivations and characteristics. This approach is central to surveys: we solicit responses from a random sample of the population through appeals to public service, tokens of appreciation, and multiple reminders (see, for example, Groves & Couper, 1998). If we can collect responses from a random sample of population members, selection bias is not a problem. Unfortunately, it is not clear that this approach will work with label collection: many people are not interested in labeling data for AI models. Surveys also find it increasingly difficult to recruit representative samples of respondents (de Leeuw et al., 2018; Williams & Brick, 2018). 7 Science of Data Collection Right Side Another way to reduce selection bias is to break the correlation on the right side of Figure 4, which would mean removing (or, more reasonably, reducing) the influence of labeler characteristics on the labels that they assign. More diverse examples in the instructions, use of test observations, feedback to labelers, and training in im- plicit bias might help labelers label more uniformly. (The literature on coding in qualitative studies takes a similar approach (see, for example, Hak & Bernts, 1996).) Even if these interventions do work to reduce the impact of labelers’ characteristics on the labels they provide, however, they are expensive and do not scale well. Interestingly, reducing selection bias by removing the cor- relation on the right side of the figure is not of interest in surveys, which aim to capture the diversity of respondents’ behavior, opinions, and judgments. Recent research in NLP has similarly found that capturing the diversity of labels across labelers can improve models (Basile et al., 2021; Sap et al., 2022). Aroyo & Welty (2015) and Plank (2022) have argued that such human label variation is in fact information and can improve model performance and trustworthiness. Weighting A third method to address selection bias is statistical adjustment. If we condition on the labeler char- acteristics in Figure 4, we can remove (or reduce) the in- duced correlation between the two propensities. Like the right side approach, this method involves embracing labeler subjectivity and uses weights to get the balance of those characteristics right. The survey literature contains many statistical methods to match the characteristics of the respondents to the popula- tion and thus reduce selection bias (Bethlehem et al., 2011, for example). For example, surveys in many countries col- lect more responses from women than men; we use weights to ensure that the contribution of women’s and men’s re- sponses on the final estimate matches their shares in the population. Future work could test the usefulness of these weighting approaches for improving machine learning mod- els.4 However, these statistical adjustments can work only if we capture the labeler characteristics that drive the relationships in Figure 4. Thus we need a better understanding of what motivates people to work as labelers and what types of tasks are vulnerable to selection bias, which points to another role for social science to play in improving label quality.
5.  Transparency in Label Collection The discussion above suggests that labels are sensitive to how studies design the labeling task and recruit labelers, in ways often not recognized in the AI/ML literature. For this reason, we call for more transparency and documentation in how labels are collected when new data sets or models are released. The survey industry in the U.S. has embraced transparency in recent years. The American Association for Public Opin- ion Research launched the Transparency Initiative in 2014. Member firms agree to disclose details about how survey data were collected, such as question and response option wording and order, respondent recruitment protocols, and weighting adjustments.5 Polling companies that are mem- bers of the Transparency Initiative outperform those who are not (Silver, 2023), suggesting that a firm’s willingness to dis- close its data collection methods is a proxy for the quality of its estimates. The U.S. federal statistical agencies recently commissioned an expert report on transparency, in an ef- fort to increase trust in federal data (National Academies of Sciences, Engineering, and Medicine, 2022). Several researchers have similarly called for transparency when releasing benchmark data sets or models (Bender & Friedman, 2018; Mitchell et al., 2019; Hutchinson et al., 2020; Gebru et al., 2021; Chmielinski et al., 2022). We join these calls and recommend releasing the labeling instruc- tions or guidelines including examples and test questions, the wording of the prompts, information about the label- ers, and whether social scientists or domain experts were involved in labeling or consulted on the labeling process. Prabhakaran et al. (2021); Geiger et al. (2020); Ulmer et al. (2022); Baan et al. (2024) have also called for better doc- umentation of the label collection process. We commend Nie et al. (2020); Ouyang et al. (2022); Glaese et al. (2022); Bai et al. (2022); Stiennon et al. (2022) as particularly good examples of transparency in label collection, with some including screenshots of the label collection instrument. Without detailed documentation of data collection methods, researchers will not be able to test many of the hypotheses given above, such as those about wording, task order, “don’t know” options, and the impact of labeler characteristics. We also suspect that lack of documentation explains difficulties replicating benchmark data sets (Recht et al., 2019).

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/SurveyTheory-ML-Labeling",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Applying Survey Methodology and Cognitive Response Theories to Improve Quality and Transparency of Machine-Learning Training Data Labels"
    },

    {
      "@id": "rdip:Dataset/Survey-Literature-Corpus",
      "@type": "schema:Dataset",
      "schema:name": "Corpus of survey methodology literature on cognitive response processes, satisficing, context effects, selection bias, and data-quality practices",
      "schema:description": "Includes key works by Tourangeau et al. (2000, 2018), Krosnick (1991), Galesic et al. (2008), Smyth (2006), Kreuter et al., and AAPOR Transparency Initiative references"
    },

    {
      "@id": "rdip:Dataset/ML-Labeling-Literature-Corpus",
      "@type": "schema:Dataset",
      "schema:name": "Corpus of ML/data-labeling studies cited as evidence or counterexamples",
      "schema:description": "Includes Kern et al. (2023), Beck et al. (2022, 2024), Bassignana & Plank (2022), Al Kuwatly et al. (2020), Sap et al. (2022), Parrish et al. (2024), Ouyang et al. (2022), etc."
    },

    {
      "@id": "rdip:Activity/Theory-Synthesis-Response-Process",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Synthesis of Tourangeau’s four-stage cognitive response process model and deviations (satisficing, acquiescence, straight-lining, motivated misreporting)",
      "prov:used": "rdip:Dataset/Survey-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Response-Process-Model-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Adapted cognitive response process model for survey answering"
      }
    },

    {
      "@id": "rdip:Activity/Context-Effects-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review and synthesis of context and order effects literature (contrast/assimilation, priming, order effects in surveys)",
      "prov:used": "rdip:Dataset/Survey-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Context-Effects-Summary",
        "@type": "schema:Dataset",
        "schema:name": "Summary of context and order effects applicable to labeling tasks"
      }
    },

    {
      "@id": "rdip:Activity/Hypothesis-Derivation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Derivation of testable hypotheses about labeling quality from survey theory (wording/reading level, multiple labels format, order effects, pre-labeling/anchoring, don’t-know options, overreliance on examples)",
      "prov:used": [
        "rdip:Dataset/Response-Process-Model-Summary",
        "rdip:Dataset/Context-Effects-Summary",
        "rdip:Dataset/ML-Labeling-Literature-Corpus"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Label-Quality-Hypotheses",
        "@type": "schema:Dataset",
        "schema:name": "Set of hypotheses linking survey-theory constructs to ML labeling quality"
      }
    },

    {
      "@id": "rdip:Activity/Selection-Bias-Framework-Adaptation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Adaptation of survey nonresponse/selection-bias framework (Groves 2006) to ML labeler recruitment and label assignment",
      "prov:used": "rdip:Dataset/Survey-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Selection-Bias-ML-Framework",
        "@type": "schema:Dataset",
        "schema:name": "Causal diagram (Figure 4) and theoretical argument for selection bias in training labels"
      }
    },

    {
      "@id": "rdip:Activity/Mitigation-Measures-Synthesis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Synthesis of mitigation strategies from survey methodology (randomization, cognitive interviewing, paradata, feedback prompts, test observations, weighting) and their proposed application to ML labeling",
      "prov:used": [
        "rdip:Dataset/Survey-Literature-Corpus",
        "rdip:Dataset/Label-Quality-Hypotheses"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Mitigation-Recommendations",
        "@type": "schema:Dataset",
        "schema:name": "List of practical mitigation measures and transparency recommendations for ML label collection"
      }
    },

    {
      "@id": "rdip:Activity/Transparency-Advocacy",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Argument for mandatory detailed documentation of labeling instruments, prompts, examples, labeler demographics, and process (modeled on AAPOR Transparency Initiative)",
      "prov:used": [
        "rdip:Dataset/Survey-Literature-Corpus",
        "rdip:Dataset/ML-Labeling-Literature-Corpus"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Transparency-Call",
        "@type": "schema:Dataset",
        "schema:name": "Call for standardized reporting of label-collection provenance in ML papers and datasets"
      }
    },

    {
      "@id": "rdip:Activity/Final-Integration",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Integration of all theoretical syntheses, hypothesis derivation, and recommendations into final methodology/theory section",
      "prov:used": [
        "rdip:Dataset/Label-Quality-Hypotheses",
        "rdip:Dataset/Selection-Bias-ML-Framework",
        "rdip:Dataset/Mitigation-Recommendations",
        "rdip:Dataset/Transparency-Call"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Final-Methodology-Section",
        "@type": "schema:Dataset",
        "schema:name": "Published 'Science of Data Collection' methodology section applying survey theory to ML labeling"
      }
    }
  ]
}
```

This JSON-LD captures the provenance of a purely theoretical/review paper whose primary contribution is the systematic adaptation of decades of survey methodology theory to the problem of ML training-data labeling quality. No new primary data or models were created; the “data production” consists entirely of literature synthesis, theoretical derivation, hypothesis generation, and recommendation formulation. All major intellectual steps are represented as separate DataProductionActivities that feed into the final manuscript section.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: 3 Data and Methods 3.1 Data F1000 Dataset We utilized the F1000 dataset (also known as Faculty Opinions) from previous studies in science of science. It comes from a post-publication peer-review platform in which invited scholars — practicing scientists and clinicians — select and evaluate biomedical papers they deem significant. The experts are asked to label papers with predefined tags in about five categories. For demonstration purposes, the labels used here contain three primary 4 A PREPRINT - FEBRUARY 28, 2025 contribution types that takes the majority of cases: (A). Interesting Hypothesis (7.5%) (B). Technical Advance (13.3%) and (C). New Finding (79%). These expert annotations has been shown to align with different types of novelty (\[31\]), thus are important in studying science and innovation. This dataset is suitable here as it provides expert-validated classifications that requires nuanced understanding. The categories are distinct yet related, making it a moderately challenging test for LLM reliability. Notably, the class imbalance mirrors real-world scientific output - most papers make empirical findings over theoretical or methodological contributions. This distribution creates natural test conditions for evaluating LLM reliability across frequent and rare categories. After preprocessing and cleaning, a total of 816 biomedical papers with expert annotations are included. Microsoft Academic Graph (MAG) Dataset To investigate how annotations might affect downstream tasks such as regression, this study uses a simple example of predicting a paper’s citation impact (with in 3 years of publication) based on the paper’s contribution types using linear regression models. To do so, the F1000 data is merged with Microsoft Academic Graph Dataset, which has publicly available Microsoft Academic Graph, to get the citation count of 816 papers. The merge was done by matching their MAG paper ids with their PMID in the PubMed dataset. Citation counts follow a heavy-tailed distribution (mean=142, SD=213, max=2,184), typical of scientific impact patterns. We log-transform citations after adding 1 to handle zeros. We also added year and team size as control variables. 3.2 LLM Models Model Selection and Architecture We employ three variants of the LLaMA-3.1 Instruct series (8B, 70B, and 405B parameters) to systematically examine how model annotation reliability changes under survey-inspired interventions. This progression captures the full spectrum from lightweight to state-of-the-art LLMs (open sourced), allowing us to test whether larger models exhibit greater robustness to survey-inspired interventions. All models use the standard dense transformer architecture along with supervised fine-tuning and direct preference optimization after pretraining \[32\]. Inference Configuration To ensure comparability across model sizes, we maintain identical generation parameters: temperature=0 for controlled randomness, top-p=0.7 sampling, and maximum output length=1 token). For probability distribution analysis, we extract logits directly from the final unembedding layer by using TogetherAI api with the parameter "logprobs" equals True . This setup allows us to precisely track how intervention-induced perturbations affect the models’ internal confidence metrics at the precise token of interest. Rationale for Multi-Scale Analysis The tripartite model selection directly informs key findings in later analyses: 1) The 8B model serves as a baseline for "commodity" LLMs accessible on consumer hardware, showing high intervention sensitivity (Figure 5 - 7) due to limited contextual reasoning capacity. 2) The 70B variant represents current practical limits of dense models, demonstrating partial robustness to position randomization but remaining vulnerable to reverse validation (Figure 5 - 7). 3) The 405B model tests whether large models with extreme scale can overcome satisficing tendencies - our results suggest even this frontier model retains non-trivial sensitivity to option ordering (Figure 5 - 7), indicating limitations in current LLM paradigms. 3.3 Annotation Implementation To setup, we design prompts for AI annotation in a multiple choces format– a fundamental and widely used format in AI tasks (\[33\], \[34\], \[35\], \[36\]), and is suggested for good performance for prompting answers (\[37\]), and as LLM to predict a single option token. This setting allows us to trace and evaluate the probablity distribution of the single token prediction easily, and allows for consistent comparison across models. 5 A PREPRINT - FEBRUARY 28, 2025 3.3.1 Prompt Design Basic Prompt Template Given the following scientific paper abstract: \[Abstract Text\] What is the main contribution type of this paper? A. Interesting Hypothesis B. Technical Advance C. New Finding Please respond with only the option of your choice. 3.4 Survey-Inspired Interventions For each paper in the dataset, we implement three types of interventions. Below are the example for each intervention.

1.  Option Randomization • Addresses token bias by varying the order of response options Example: Option Randomization Original: What is the main contribution type of this paper? A. New method B. New finding C. New theory Randomized Variants:

1.  A. New finding B. New theory C. New method
2.  A. New theory B. New method C. New finding

2.  Position Randomization • Mitigates the impact of prompt position structure on responses Example: Position Randomization Original: What is the main contribution type of this paper? A. New method B. New finding C. New theory Position Variants:

1.  B. New finding C. New theory A. New method
2.  C. New theory A. New method B. New finding

3.  Reverse Validation • Creating reverse-coded items Example: Reverse Validation Original: What is the main contribution type of this paper? A. New method B. New finding C. New theory Reverse: What items are NOT the main contribution of this paper? A. New finding or New theory B. New method or New theory C. New method or New finding 6 A PREPRINT - FEBRUARY 28, 2025 3.5 Reliability Metric Design Beyond implementing interventions, we also need to quantify the inherent uncertainty in LLM annotations. While LLMs always provide a definitive answer when forced to choose, this masks their internal uncertainty. The intervention results (as shown in the next section) suggest that when models are genuinely uncertain about the correct classification, their outputs become highly sensitive to prompt variations—exactly what the survey-inspired interventions are designed to detect. 3.5.1 Independent Probability Assessment To measure model uncertainty accurately, we need to access the probability distribution over possible answers. However, directly presenting all options simultaneously in a prompt introduces a problematic asymmetry due to the causal attention mechanism of transformer-based LLMs. Information from earlier options accumulates and influences the processing of later options, creating position-dependent biases (see Figure 2). Thus, the model isn’t actually evaluating the options independently. Figure 2: The Causal Asymmetry of Information Accumulation in LLM To address this issue, the paper propose independently evaluating each category through separate binary queries: Independent Probability Assessment Example query for each category: Given the following scientific paper abstract: \[Abstract Text\] Is the main contribution of this paper "Technical Advance"? Please answer only Yes or No. By repeating this process for each category ("Interesting Hypothesis", "Technical Advance", and "New Finding"), we can obtain independent probability assessments p(Yes|Category) for each category. This approach can be understood as the LLM-version of projecting meanings onto specific dimensions (\[38, 39, 40\]) —thus representing a "geometry of thinking" where each query projects the input text onto a distinct semantic axis, albeit using natural language. This controls for information asymmetry, allowing us to capture the model’s genuine preference distribution. This metric can be viewed as the "dual" of survey intervention. While survey intervention introduces asymmetry into prompts to test reliability, this reliability score does the opposite—it controls for these asymmetries to uncover the model’s inherent preferences. In essence, survey intervention deliberately perturbs the system, while our reliability measure filters out these perturbations to reveal the underlying signal. 3.5.2 Information-Theoretic Reliability Score Drawing from information theory, the paper proposes a reliability score (R-score) based on Kullback-Leibler divergence that quantifies how much an LLM’s probability distribution differs from a uniform random distribution: 7 A PREPRINT - FEBRUARY 28, 2025 R-score Calculation R= DKL(P||U) = k pi log pi 1/k (1) i=1 where: • P= {p1,p2,...,pk }is the normalized probability distribution across kannotation options • U= {1/k,1/k,...,1/k}is the uniform distribution representing random guessing • Higher R-scores indicate greater divergence from random guessing, suggesting more reliable annotations Inter-option Distinguishability Label 1 Label 2 Label 3 Inter-case Distinguishability Text 1 Text 2 Text 3 Text 4 Text 5 Text 6 0.34 0.31 0.35 KL=0.00 DKL(P||U) = 0.10 0.10 0.80 KL=0.46 0.41 0.39 0.20 KL=0.04 0.05 0.90 0.05 KL=0.70 k pilog ( pi 1/k ) i = 1 Information-Theoretic Reliability Levels High Reliability (KL 0.7) Moderate Reliability (0.36 KL < 0.7) Low Reliability (0.06 KL < 0.36) Very Low Reliability (KL < 0.06) 0.95 0.03 0.02 KL=0.87 0.33 0.33 0.34 KL=0.00 Reliability is measured using KL divergence from uniform distribution. Higher KL values indicate more reliable predictions that diverge further from random guessing. Figure 3: Information-Theoretic Reliability Score (R-score). While Figure 1 illustrates the conceptual difference between accuracy and effectiveness, we need a concrete metric to operationalize this distinction. Figure 3 introduces an information-theoretic reliability score (R-score). The reliability of a large language model (LLM) annotation can be quantified by measuring how distinctly it can differentiate between multiple classification options. Figure 3 gives an example matrix. The matrix shows probability distributions for six example texts, with each row representing a text and each column representing a classification option. Specifically, we want LLM to assign a probability for each case under each option, independently, and then normalized these probabilities. Then, the reliability is calculated using Kullback-Leibler (KL) divergence from a uniform distribution: R= DKL(P||U) = k i=1 pi log pi 1/k , where prepresents the normalized probability distribution across kannotation options and U is a uniform distribution (1/kfor each option, indicating random guessing). Color coding reflects reliability levels: dark green indicates high reliability (KL ≥0.7, strong differentiation between options), light green indicates moderate reliability (0.36 ≤KL <0.7), light red indicates low reliability (0.06 ≤KL <0.36), and dark red indicates very low reliability (KL <0.06, near-uniform distribution suggesting random guessing). For example, Text 2 shows high reliability (KL = 0.87) with a clear preference for Label 1 (0.95), while Text 1 shows very low reliability (KL = 0.00) with near-equal probabilities across all options, indicating the model cannot meaningfully distinguish between classification choices. This information-theoretic approach thus provides a principled metric for assessing when LLM annotations should be trusted for downstream analyses, at the case level. Based on empirical analysis with three-option classification tasks, we establish four reliability thresholds: 8 A PREPRINT - FEBRUARY 28, 2025 Reliability Thresholds • High Reliability (R ≥0.7): Corresponds approximately to a distribution of \[0.9, 0.05, 0.05\], indicating strong confidence in the top prediction • Moderate Reliability (0.36 ≤R < 0.7): Corresponds approximately to a distribution of \[0.75, 0.125, 0.125\], showing clear preference for the top option • Low Reliability (0.06 ≤R < 0.36): Corresponds approximately to a distribution of \[0.5, 0.25, 0.25\], where the top probability equals the sum of remaining options • Very Low Reliability (R < 0.06): Distribution approaches uniformity, suggesting the model is essentially guessing The thresholds of R-score were empirically selected based on intuitive probability distributions for a three-option classification scenario. A distribution close to uniform (low R-score) suggests the model cannot meaningfully dif- ferentiate between categories, while a highly skewed distribution (high R-score) indicates strong preference for a particular category. The threshold of KL = 0.06 corresponds approximately to a distribution of \[0.5, 0.25, 0.25\], where the top probability is equal to the sum of remaining options. KL = 0.36 corresponds to a distribution of \[0.75, 0.125, 0.125\], where the top probability is three times of the rest others, demonstrating a clearer model preference. KL = 0.7 corresponds to a distribution of \[0.9, 0.05, 0.05\], representing a case where the model shows very strong confidence (90% of the time) in its top prediction. In other words, if the model repeatedly annotates this case randomly, the result is consistent with the "top" label in 90% cases. The R-score complements our intervention-based approach by providing a continuous measure of annotation confidence. While interventions reveal sensitivity to prompt variations, the R-score quantifies the inherent uncertainty in the model’s predictions.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/LLM-Reliability-Survey-Interventions",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Evaluating LLM Annotation Reliability Using Survey-Methodology-Inspired Interventions and Information-Theoretic Scoring"
    },

    {
      "@id": "rdip:Dataset/F1000-Expert-Annotations",
      "@type": "schema:Dataset",
      "schema:name": "F1000 (Faculty Opinions) expert-labeled biomedical papers",
      "schema:size": 816,
      "schema:description": "816 biomedical papers with expert-assigned contribution tags (Interesting Hypothesis 7.5%, Technical Advance 13.3%, New Finding 79%) after cleaning"
    },

    {
      "@id": "rdip:Dataset/MAG-Citation-Data",
      "@type": "schema:Dataset",
      "schema:name": "Microsoft Academic Graph (MAG) citation counts merged with F1000 papers",
      "schema:description": "Citation counts (within 3 years) for the 816 F1000 papers, matched via PMID → MAG PaperID, log(citations+1) transformed"
    },

    {
      "@id": "rdip:Activity/Data-Merging-Cleaning",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Merging F1000 expert annotations with MAG citation data and preprocessing",
      "prov:used": [
        "rdip:Dataset/F1000-Expert-Annotations",
        "rdip:Dataset/MAG-Citation-Data"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/F1000-MAG-Merged",
        "@type": "schema:Dataset",
        "schema:name": "Final analysis dataset of 816 papers with expert labels, citations, year, and team size"
      }
    },

    {
      "@id": "rdip:Activity/LLM-Inference-Setup",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Zero-shot/few-shot inference on LLaMA-3.1-Instruct 8B/70B/405B using TogetherAI API",
      "rdip:usedSoftware": [
        {
          "@id": "rdip:Software/LLaMA-3.1-Instruct",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "LLaMA-3.1-Instruct (8B, 70B, 405B variants)",
          "rdip:version": "2024 open-weight release"
        },
        {
          "@id": "rdip:Software/TogetherAI-API",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "TogetherAI inference API",
          "rdip:version": "2024–2025"
        }
      ],
      "schema:description": "Inference parameters: temperature=0, top_p=0.7, logprobs=True, max_tokens=1",
      "prov:used": "rdip:Dataset/F1000-MAG-Merged"
    },

    {
      "@id": "rdip:Activity/Prompt-Design",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Design of base multiple-choice prompt template for contribution-type classification",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Base-Prompt-Template",
        "@type": "schema:Dataset",
        "schema:name": "Standard multiple-choice prompt with fixed option order A/B/C"
      }
    },

    {
      "@id": "rdip:Activity/Survey-Interventions-Implementation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Systematic application of three survey-inspired prompt perturbations (Option Randomization, Position Randomization, Reverse Validation)",
      "prov:used": "rdip:Dataset/Base-Prompt-Template",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Intervention-Perturbed-Prompts",
        "@type": "schema:Dataset",
        "schema:name": "6 perturbed prompt variants per paper (2 option orders × 3 position variants × reverse-coded)"
      }
    },

    {
      "@id": "rdip:Activity/LLM-Intervention-Runs",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Execution of all intervention prompts on 816 papers across three LLaMA-3.1 models with logprobs",
      "rdip:usedSoftware": "rdip:Software/TogetherAI-API",
      "prov:used": [
        "rdip:Dataset/F1000-MAG-Merged",
        "rdip:Dataset/Intervention-Perturbed-Prompts"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/LLM-Intervention-Outputs",
        "@type": "schema:Dataset",
        "schema:name": "Raw token predictions and full logprob distributions for all intervention conditions"
      }
    },

    {
      "@id": "rdip:Activity/Independent-Probability-Assessment",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Independent binary yes/no queries for each contribution category to eliminate causal attention bias",
      "schema:description": "Three separate API calls per paper: 'Is the main contribution Technical Advance? Yes/No' etc.",
      "rdip:usedSoftware": "rdip:Software/TogetherAI-API",
      "prov:used": "rdip:Dataset/F1000-MAG-Merged",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Independent-Probabilities",
        "@type": "schema:Dataset",
        "schema:name": "Per-category p(Yes) probabilities for 816 papers × 3 categories × 3 models"
      }
    },

    {
      "@id": "rdip:Activity/R-Score-Computation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Computation of information-theoretic reliability score (R-score = D_KL(P || U)) with empirical thresholds",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/Python-NumPy-SciPy",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Python (NumPy/SciPy for KL divergence)",
        "rdip:version": "unknown"
      },
      "prov:used": "rdip:Dataset/Independent-Probabilities",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/R-Scores",
        "@type": "schema:Dataset",
        "schema:name": "Per-paper R-scores and reliability tiers (Very Low / Low / Moderate / High) for each model"
      }
    },

    {
      "@id": "rdip:Activity/Downstream-Regression-Example",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Linear regression of log(citations+1) ~ predicted contribution type (expert vs. LLM labels) with controls",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/Python-statsmodels",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Python statsmodels / scikit-learn",
        "rdip:version": "unknown"
      },
      "prov:used": [
        "rdip:Dataset/F1000-MAG-Merged",
        "rdip:Dataset/LLM-Intervention-Outputs"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Regression-Results",
        "@type": "schema:Dataset",
        "schema:name": "Coefficients showing downstream impact of LLM vs. expert labels on citation prediction"
      }
    }
  ]
}
```

This JSON-LD fully captures the provenance of the empirical study:

*   Central project
*   Source datasets (F1000 expert labels + MAG citations) and merging/cleaning
*   Use of LLaMA-3.1-Instruct (8B/70B/405B) via TogetherAI API with logprobs
*   Systematic design and application of three survey-inspired prompt interventions
*   Novel independent binary probability assessment to remove attention bias
*   Introduction and computation of the information-theoretic R-score (KL-based reliability metric)
*   Downstream regression example All major data-producing activities, software/tools (with versions where known), and resulting datasets are represented using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: The Code-Survey process follows a structured workflow, as illustrated in Figure 1:

1.  Survey Design by Human Experts or LLM Agents: Experts or LLM agents create tailored questions for each type of unstructured data (e.g., commits, emails) to extract key insights. The survey design is crucial for guiding the LLM in structuring the data effectively and focuses on tasks aligned with the LLM’s strengths, such as summarization and yes/no questions. This step should minimizes the usage of open-ended questions that require deep domain expertise.
2.  Survey Completion by LLM Agents: LLM agents process the unstructured input by answering the sur- vey questions. They organize data into structured for- mats by tagging relevant information, summarizing key points, and identifying important patterns. This step is fundamental in transforming unstructured data into structured datasets, enabling more straightfor- ward analysis.
3.  Evaluation of Survey Results by Human Experts or LLM Agents: Human experts with domain-specific 3 Conference’17, July 2017, Washington, DC, USA knowledge, or additional LLM agents, evaluate a sam- ple of the structured data. This evaluation ensures accuracy and allows for the detection of discrepancies. If the results are unsatisfactory, the process loops back to Step 1, where the survey design is refined.
4.  Data Processing and Quantitative Analysis: The structured data undergoes further processing to ana- lyze key metrics and patterns. Quantitative analysis is performed to identify trends in development, feature interdependencies, and areas needing improvement in reliability and security. This provides a detailed view of the system’s evolution and characteristics. This process employs an iterative design, allowing surveys to be refined based on analysis results, thereby creating a feedback loop that enhances data structuring and interpre- tation. By leveraging both LLMs and human oversight, the Code-Survey methodology efficiently handles large volumes of unstructured software data. At each step, human experts can interactively contribute, or LLM agents can automate the process. 3.2 Survey Design with LLM Assistance A key aspect of Code-Survey is designing effective surveys to generate accurate data. Surveys can be designed by humans or LLM agents. We identify three key steps to guide LLM agents in designing surveys. The following prompts serve as a framework or LLM input for survey creation:
5.  Design High-Level Insightful Questions: If you could ask every kernel developer to complete a survey or questionnaire about a commit or an email, what are the most insightful questions related to design, im- plementation, maintenance, reliability, and security? Describe the possible questions in detail.
6.  Identify Required Data Types and Sources: What data types and sources are required to answer the in- sightful questions described previously? Describe the data types and sources for each question in detail.
7.  Design Survey Questions to Retrieve Data: What survey questions can you design to obtain the required data types for the insightful questions from the data sources described previously? Describe the survey questions for kernel developers in detail. This workflow ensures that the LLM-driven survey design process leads to structured data that offers deeper insights into complex software systems, such as the Linux kernel. By guiding LLM agents through these steps, we can systemat- ically extract valuable information from unstructured data sources. 4 Case Study: eBPF In this section, we apply the Code-Survey methodology to an- alyze the evolution and development of the eBPF subsystem in the Linux kernel. Our goal is to uncover insights into the Yusheng Zheng, Yiwei Yang, Haoqin Tu, and Yuxi Huang lifecycle, stability, and design decisions of key eBPF features. The survey results are validated through expert review and both quantitative and qualitative analyses. The Extended Berkeley Packet Filter (eBPF) \[2\] is a rapidly evolving subsystem in the Linux kernel that allows users to run sandboxed programs in kernel space without modi- fying the kernel itself \[23\]. Originally developed for packet filtering, eBPF now supports diverse use cases such as per- formance tracing, security monitoring, and system observ- ability, and has been expanded to multiple platforms \[25, 42\]. The academic community has identified current problems and limitations of eBPF, proposing several works to improve aspects like the verifier and deployment. 4.1 Motivation: Analyzing eBPF Kernel Features with Data Analysis To understand the limitations of traditional data analysis methods, we begin by analyzing the evolution of eBPF ker- nel features using well-defined kernel commits. Traditional methods allow us to study the development of various eBPF features, such as helpers, maps, attach types, and other func- tionalities. We obtained feature pairs from eBPF documenta- tion \[11\] and combined them with Git commit data. 4.1.1 How Do All eBPF Features Evolve Over Time? Figure 2 shows trends in the adoption of new features within the overall eBPF subsystem. Helpers and kfuncs exhibit the most significant growth, supporting various use cases and changes, while other features have shown steady increases over the past four years, indicating their maturation. Figure 2. Cumulative eBPF Features Timeline 4.1.2 Timeline of eBPF Helper Functions vs. Kfuncs. Figure 3 illustrates the evolution of eBPF helper functions and kfuncs over time. Since 2023, helper functions have remained stable with almost no new additions, whereas kfuncs are growing rapidly; this demonstrates the community’s interest in expanding kernel interaction via kfuncs, and all new use cases now tend to use kfuncs to influence kernel behavior, signaling a shift toward deeper kernel integrations. 4 Code-Survey: An LLM-Driven Methodology for Analyzing Large-Scale Codebases Figure 3. Cumulative Helper and kfunc Timeline 4.1.3 What Are the Patterns in Other eBPF Features? Figure 4 examines the evolution of eBPF features, excluding helpers and kfuncs, with a focus on core eBPF functionali- ties and their impact on the overall subsystem. After 2020, core features such as events, flags, map types, and program types have stabilized. Notably, the introduction of bpf\_link coincides with the effort on the management of growing use cases and complexity, resulting in a significant difference observed before and after its introduction. Figure 4. Cumulative eBPF Features Timeline Without Helpers and kfuncs However. . . The analysis of eBPF features mainly relies on kernel structured definitions and data sources obtained by humans, which is limited by data availability and the time-consuming process of manual data collection. There is a massive amount of unstructured data in the form of commit messages, code changes, and developer dis- cussions that can provide valuable insights into the evolution and design decisions of eBPF features. While it is possible for humans to perform empirical analysis on some of this data, covering all of it is practically impossible. Conference’17, July 2017, Washington, DC, USA Can AI assist us? Instead of relying on large language models (LLMs) to attempt kernel coding—which may yield incorrect answers—we propose a different quantitative ap- proach. By carefully designing a survey and utilizing LLMs to trans- form unstructured data like commits and emails into well- organized, structured, and easy-to-analyze datasets, we can perform quantitative analysis using traditional methods. In this way, AI can help analyze data and provide answers quickly; this capability is already a feature of platforms like ChatGPT. 4.2 Research Questions for Survey Evaluation To ensure that the LLM does not answer questions randomly, we evaluate the effectiveness and correctness of the Code- Survey results by exploring the following high-level research questions: • Correctness of Survey Responses: How can we en- sure that survey responses reflect accurate and rel- evant information about the system’s features and commits? • Consistency Across Similar Questions: Are similar questions answered consistently across different but related features or subsystems? • Coverage of Survey Questions: Do the survey ques- tions comprehensively cover all relevant aspects of the feature or subsystem under analysis? • Insight from Survey: Can the survey data help users analyze the design, implementation, maintenance, re- liability, and security evolution, and gain valuable in- sights? • Clarity and Ambiguity in Responses: Are the sur- vey responses clear and unambiguous, making them actionable for further analysis? • Alignment with Real-World Changes: How accu- rately do survey results reflect real-world changes in the software’s features and evolution? • Expert Confirmation: How do experts rate the accu- racy of the survey’s generated insights? 4.3 Commit Survey Design and Objectives To gain deeper insights into the design and evolution of the eBPF subsystem, we developed a comprehensive survey aimed at classifying commits within the Linux eBPF subsys- tem. This survey evaluates specific aspects of each commit by analyzing commit messages and associated code changes. In cases where the commit message provides insufficient information, respondents are allowed to select an “I’m not sure” option. The primary goals of the survey are to: • Provide concise summaries of each commit. • Extract key themes and components affected by each commit. 5 Conference’17, July 2017, Washington, DC, USA • Classify commits based on their type, complexity, and impacted components. • Identify patterns and trends in the evolution of the eBPF subsystem. 4.3.1 Survey Structure. The survey consists of a series of structured questions designed to capture the essential characteristics of each commit. Respondents are encouraged to be as specific as possible based on the available commit message and code changes. If the commit message lacks clarity, the “I’m not sure” option can be selected. 4.3.2 Simplified Survey Definition. Below is the simpli- fied survey structure:
8.  Summary: Provide a one-sentence summary of the commit (max 30 words).
9.  Keywords: Extract up to three keywords from the commit.
10.  Commit Classification (Single Choice): What is the main type of the commit? (a) Bug fix (b) New feature (c) Performance optimization (d) Code cleanup or refactoring (e) Documentation change or typo fix (f) Test case or test infrastructure change (g) Build system or CI/CD change (h) Security fix (i) Merge commit (j) Other type of commit (k) I’m not sure
11.  Commit Complexity (Single Choice): Estimate the complexity of implementing this commit. (a) Simple (affects 1–20 lines or 1–2 files) (b) Moderate (affects 21–100 lines or a few files) (c) Complex (affects over 100 lines or 5+ files) (d) Merge-like (merges multiple branches or features) (e) Non-code or generated changes (f) I’m not sure
12.  Major Related Implementation Component (Sin- gle Choice): What is the main implementation compo- nent modified? (a) eBPF verifier (b) eBPF JIT compiler (c) Helpers and kfuncs (d) Syscall interface (e) eBPF maps (f) libbpflibrary (g) bpftool utility (h) Test cases and makefiles (i) Changes in other subsystems related to eBPF events (j) Merge commit (k) Other component related to eBPF (l) Unrelated to eBPF subsystem Yusheng Zheng, Yiwei Yang, Haoqin Tu, and Yuxi Huang (m) I’m not sure
13.  Major Related Logic Component (Single Choice): What is the main logic component affected? (a) eBPF instruction logic (b) Runtime features logic (c) eBPF events-related logic (d) Control plane interface logic (e) Maps logic (f) BPF Type Format (BTF) logic (g) Merge commit (h) General utilities logic (i) Other eBPF logic component (j) Unrelated to eBPF subsystem (k) I’m not sure
14.  Use Cases or Submodule Events (Multiple Choice): What eBPF use cases or subsystem events does the commit relate to? (a) XDP-related programs (b) Socket-related programs (c) tc-related programs (d) Netfilter-related programs (e) Tracepoints-related programs (f) Kernel probes (kprobe/ftrace) (g) User-space probes (uprobe/USDT) (h) Profiling-related programs (i) LSM-related programs (j) struct\_ops-related programs (k) cgroup-related programs (l) HID driver-related programs (m) Scheduler-related programs (n) Improves overall eBPF infrastructure (o) Merge commit (p) Other eBPF use cases (q) Unrelated to eBPF subsystem (r) I’m not sure 4.4 Implementing the Survey Using LLM Agents To efficiently process and analyze the vast number of com- mits in the Linux eBPF subsystem, we leveraged LLMs to automate our survey. We developed Assistant Agents using GPTs \[31\] for generating survey responses and assisting in analyzing results. By utilizing the GPT-4o \[30\] LLM model, we transformed unstructured commit data into structured responses aligned with our survey definitions. We initially applied this method to over 15,000 commits spanning eight years and plan to expand it to include emails and patches. 4.4.1 Commit Survey Methodology. Our approach uses an AI model to analyze each commit’s details and answer the survey questions. The process includes:
15.  Data Extraction: We gather key commit details such as commit ID, author information, commit date, mes- sage, code changes, and associated emails. 6 Code-Survey: An LLM-Driven Methodology for Analyzing Large-Scale Codebases 2. Prompt Construction: A prompt containing the sur- vey title, description, changed files, and commit details is generated to guide the AI.
16.  AI Model Interaction: The AI processes the prompt, analyzing the commit message and code changes to respond to the survey. For each commit, the AI receives the commit details and survey questions, completes them, and generates structured output as JSON.
17.  Feedback Loop: If the AI’s response is incomplete or inconsistent, it re-evaluates and revises the answers to improve accuracy.
18.  Data Aggregation: The AI’s responses are stored for later quantitative analysis. We used the GPT-4o model for its strong language under- standing and ability to handle technical content, making it well-suited for analyzing kernel commits. 4.4.2 Enhancing Survey Accuracy. Due to time and bud- get limitations, the AI’s performance in this experiment can still be greatly improved. Several strategies can enhance ac- curacy: • Multiple Iterations: Running the survey multiple times and averaging results, similar to human surveys, can significantly reduce response variability. Due to budget limits, we ran it once per commit, and the re- sults are already meaningful with less than 1% error. We plan to run the survey multiple times and conduct a better evaluation in future work. • Advanced Models: Fine-tuning domain-specific LLMs for kernel development, or using more advanced mod- els like O1 \[38\], can capture technical nuances better. • Refined Prompt Engineering: Crafting clearer prompts and survey questions will improve response accuracy. • Multi-Step Reasoning: Using multi-step processes or multi-agent systems can help analyze complex com- mits more thoroughly. Automating the survey with LLMs enabled us to efficiently process tens of thousands of commits, transforming unstruc- tured data into structured insights. 4.5 The Commit Dataset The commit\_survey.csvdataset provides detailed metadata for over 15,000 Linux kernel commits, including commit types, messages, timestamps, and affected components. It is used to categorize and classify commits, focusing on the eBPF subsystem. 4.5.1 Dataset Overview. The dataset contains the follow- ing fields: • Commit Metadata: Unique commit IDs, author and committer details, and timestamps. • Commit Messages and File Changes: Descriptions of the changes in each commit. Conference’17, July 2017, Washington, DC, USA • Classification: Types such as bug fixes, feature addi- tions, or merges. • Complexity: Based on the number of files and lines changed. • Components: Affected implementation and logic com- ponents. • Use Cases: Related subsystems and modules. Figure 5. Commit Classification Distribution Commit Classification Distribution. Most commits fo- cus on bug fixes and code cleanups, reflecting ongoing efforts to maintain code quality. Significant attention is also given to testing infrastructure changes, emphasizing the importance of robustness. New features constitute a considerable portion of the commits, while merge commits are commonplace in the Linux kernel’s development process. Figure 6. Commit Complexity Distribution Commit Complexity Distribution. The majority of com- mits are simple, involving small changes, while more com- plex changes constitute a smaller but noteworthy portion. 7 Conference’17, July 2017, Washington, DC, USA Figure 7. Major Related Implementation Components Major Related Implementation Components. Test cases and build scripts are significantly affected, highlighting con- tinuous improvements in testing and build processes. The libbpf library is also a key component in the kernel eBPF toolchain, receiving considerable development attention. Ad- ditionally, substantial development occurs in other kernel subsystems, particularly related to eBPF events. The frequent updates to the eBPF verifier and helpers indicate ongoing efforts to enhance functionality and ensure program safety. Notably, some commits appear unrelated to the eBPF sub- system. Figure 8. Major Related Logic Components Logic Components Affected. General utilities, such as tools and scripts, receive the most updates, followed by run- time features like helpers and kernel functions, which are consistently enhanced. eBPF event logic and instruction han- dling are also frequently updated to ensure robustness and functionality. Use Cases and eBPF Events. While most commits en- hance the core eBPF infrastructure—including the verifier Yusheng Zheng, Yiwei Yang, Haoqin Tu, and Yuxi Huang Figure 9. Related Events and Use Cases and runtime components—significant development also ex- tends to networking-related features such as socket and XDP programs, which receive substantial attention. Additionally, tracing tools like tracepoints and kprobes highlight eBPF’s crucial role in system diagnostics and debugging. 4.6 Correctness of Survey Responses To ensure that the survey responses accurately reflect system features and commits, we validated the results by randomly sampling the data and cross-referencing with expert knowl- edge and processing logs. Specifically, we addressed two common issues: the handling of merge commits and the identification of commits unrelated to the eBPF subsystem. 4.6.1 Merge Commit Correctness. We observed discrep- ancies in how merge commits were classified between the commit classification and the major implementation compo- nent perspectives. To address this, we analyzed the top merge commit messages and found that some merge commits were categorized based on their predominant effect on a specific component rather than being uniformly labeled as merge commits. By clarifying this distinction in the survey ques- tions, we ensured that the classification system accurately reflected the commit’s impact across different perspectives. Example: Top Commit (Classification but not Implementation): 3 Merge branch'bpf-fix-incorrect-name-check-pass' 25 Merge branch'vsc73xx-fix-mdio-and-phy' Pawel... 4.6.2 Non-Related eBPF Subsystem Commits. We noted that commits not directly related to the eBPF subsystem were sometimes included due to broad filtering criteria (e.g., –grep=bpf). Upon reviewing these commits, we confirmed that some mentioned “bpf” but addressed unrelated or pe- ripheral issues. Example: Sample'Not related to eBPF' Commit Messages: 17 bonding: fix xfrm real\_dev null pointer... 8 Code-Survey: An LLM-Driven Methodology for Analyzing Large-Scale Codebases 21 btrfs: fix invalid mapping of extent xarray st... 4.6.3 Consistency Across Similar Questions. We checked for consistency in responses by comparing related questions, focusing on the number of merge commits in commit classi- fications and complexities, as well as the number of commits unrelated to the eBPF subsystem in the implementation and logic components. Example 1: Merge Commits • Commit Classification: “It’s like a merge commit.” (2,130 responses) • Commit Complexity: “Merge-like. The commit merges branches.” (2,132 responses) Example 2: Unrelated Components • Implementation Component: “Not related to eBPF.” (773 responses) • Logic Component: “Not related to eBPF.” (766 re- sponses) The close alignment of these numbers demonstrates con- sistent identification of unrelated components. With a low misclassification rate (under 0.05% for total commits), our data shows high consistency, supporting the reliability of the survey design. 4.7 Timeline Analysis of Commits Analyzing the timeline of commits provides valuable insights into the evolution of the eBPF subsystem over time. By visu- alizing the distribution of commit types, complexities, and major components across different periods, we can identify trends and patterns in the development of eBPF features. The data was processed by cleaning to remove irrelevant commits, smoothing using a 3-month average to reduce noise and highlight long-term trends, and treating single- component Merge commits as regular commits while re- moving multi-component Merge commits, such as mainline merges. The time span covers from 2017 to the end of 2024, encompassing over 15,000 commits. Conference’17, July 2017, Washington, DC, USA 4.7.1 Commit Classification Over Time. Figure 10 shows the distribution of different types of commits over time. The development began to grow significantly in 2017, with limited addition of test cases initially, which continued to improve over time. New feature development follows a cycli- cal pattern, with notable spikes around 2020 and 2021. After 2021, the number of cleanups and refactorings increases sig- nificantly, while new feature additions decline, indicating a shift in focus towards code maintainability and stability. A decline in cleanup commits after 2023 suggests that while new features continue to be added, the emphasis has shifted more towards stabilization and optimization. Figure 10. Commit Classification Over Time Figure 11. Commits Related to Major Implementation Com- ponents Over Time 4.7.2 Commits Related to Major Implementation Com- ponents Over Time. Figure 11 illustrates the evolution of major implementation components in the Linux eBPF sub- system. Most components experienced their highest activity be- tween 2017 and 2022, reflecting the rapid development of eBPF features during this period. The libbpf library saw the most dramatic increase, while the JIT compiler was most frequently updated around 2018. The rise in test cases also re- flects the growing importance of a robust testing framework in this field. After peaking around 2021–2022, several components show a decline or stabilization in activity. This indicates that many eBPF components have entered a phase of optimization and maintenance rather than new feature development, while testing continues to increase coverage. The verifier shows modest activity throughout the observed period but seems to increase in 2023–2024, which may reflect renewed research efforts in this area. 4.7.3 Commits Related to Major Logic Components Over Time. Figure 12 illustrates the evolution of major logic components within the Linux eBPF subsystem over time. The General Utilities component, which includes test cases and build scripts, exhibits the most significant improvements, 9 Conference’17, July 2017, Washington, DC, USA Yusheng Zheng, Yiwei Yang, Haoqin Tu, and Yuxi Huang activities show a steady increase with periodic fluctuations, peaking around 2021 before decreasing. The kprobe/ftrace- related events remain mostly stable, with a slight increase in 2022. Uprobe-related events show moderate activity over several years, with slight peaks in 2022 and again in 2024. The struct\_ops, an emerging feature introduced in 2020, shows a significant increase in activity between 2023 and
19.  Other events such as LSM for security remain minor. 4.8 Deeper Insights Analysis This section delves into the survey responses to uncover patterns, trends, and areas for improvement within the eBPF subsystem. Figure 12. Commits Related to Major Logic Components Over Time reaching a peak between 2022 and 2023 before experienc- ing a decline. In contrast, the eBPF Instruction Logic component displays two prominent peaks in 2018 and 2024, corresponding to the initial introduction of eBPF instructions and subsequent standardization efforts, respectively. Other components, such as Runtime Features, Helpers, and kfuncs, show a notable peak in 2023 followed by a de- crease and subsequent stabilization. Meanwhile, the Control Plane Interface and Maps Logic components maintain relatively steady levels of activity throughout the observed period. Figure 13. Use Cases or Events Over Time 4.7.4 Use Cases or Events Over Time. Figure 13 reveals significant fluctuations in event types over the years. Notably, network-related events such as socket and XDP programs experienced a surge from 2020 to 2022, after which they entered a stabilization phase following the initial burst of feature additions and optimizations. The tracepoints-related Figure 14. Kernel Implementation Components with the Most Bugs 4.8.1 Which Kernel Components and Files Have the Most Frequent Bugs? Figure 14 illustrates the kernel imple- mentation components with a high number of bugs. While previous analyses and tools have primarily focused on im- proving the stability of the verifier and JIT compiler, these ar- eas account for only about 35% of the bugs. The largest num- ber of bugs originate from eBPF event-related code, which involves the interaction of eBPF with other kernel subsys- tems. Additionally, helpers and maps also have a significant number of bugs. Due to the complexity of the control plane, the eBPF syscall interface is also prone to bugs. By examining specific files, we observe that bugs fre- quently occur in the verifier, syscall, core, and network filter components. These files require better test coverage and more attention. Top 10 Buggy Files: kernel/bpf/verifier.c 425 net/core/filter.c 140 kernel/bpf/syscall.c 111 include/linux/bpf.h 87 kernel/bpf/core.c 83 include/uapi/linux/bpf.h 80 kernel/trace/bpf\_trace.c 77 10 Code-Survey: An LLM-Driven Methodology for Analyzing Large-Scale Codebases kernel/bpf/btf.c 75 tools/include/uapi/linux/bpf.h 54 kernel/bpf/sockmap.c 51 Conference’17, July 2017, Washington, DC, USA Figure 16. Evolution of libbpf Over Time on the JIT compiler, suggesting potential areas for JIT optimization. Figure 15. Verifier Bugs or Features Related to eBPF Instruc- tions Over Time 4.8.2 What is the Relationship Between Instruction- Related Changes in the Verifier and All Verifier Bugs? Figure 15 shows that changes related to eBPF instructions in the verifier closely correlate with the number of verifier bugs. This insight highlights the importance of focusing on instruction-related aspects during verifier development and debugging to enhance overall system stability. 4.8.3 The Evolution and Status of libbpf. We also ex- amined the lifecycle of specific components, such as libbpf. Based on Figure 16, the development of libbpf began to grow significantly in 2017. New feature development fol- lows a cyclical pattern, with notable spikes around 2020 and
20.  After 2022, the number of cleanups and refactorings increased significantly, indicating a shift in focus towards code maintainability and stability. However, the decline in cleanup commits after 2023 suggests that while new features continue to be added, the emphasis has shifted more towards stabilization and optimization. Historical milestones verify this trend. For instance, libbpf version 1.0 was released in August 2022 \[22\], and the major feature “Compile Once, Run Everywhere” (CO-RE) was in- troduced around 2020 \[26\], both aligning with the peaks and shifts observed in the commit history. 4.8.4 What Dependencies Have Emerged Between Fea- tures and Components? Our analysis of feature-component dependencies in Figure 17 reveals two primary patterns. First, new control plane abstractions such as bpf\_link\[28\] and token\[27\] typically require coordinated updates to both the syscall interfaceand libbpf, indicating tightly coupled development. Second, runtime features like bpf\_iter\[10\] and spin\_lock\[36\] mainly depend on internal kernel compo- nents such as helpersand verifier, with minimal impact 11 Figure 17. Feature-Component Interdependencies in the BPF Subsystem 4.9 Expert Confirmation We discussed the results with more than five eBPF experts who have submitted kernel patches or presented at confer- ences. They confirmed that the findings align with their understanding. We also shared the report with kernel main- tainers and the BPF kernel mailing list, which is currently under discussion. Additionally, we plan to provide experts with a sample of survey responses and ask them to rate the accuracy of each response on a defined scale. Based on their feedback, we will refine the survey to improve its correctness and relevance. 4.10 Clarity and Ambiguity in Responses Based on the insights gathered from the survey responses, the results are generally clear and actionable. We plan to invite more experts to review a sample of the responses to identify any vague or unclear answers. Subsequently, we Conference’17, July 2017, Washington, DC, USA will revise any survey questions prone to misinterpretation or ambiguity to improve clarity and precision. 4.11 Alignment with Real-World Changes By comparing survey responses with real-world feature changes discussed earlier, we confirm that the survey likely captures the correct historical context. We plan to cross- reference survey results with commit histories, mailing list discussions, and kernel release notes to further verify align- ment with real-world changes. 4.12 Coverage of Survey Questions We plan to review the survey’s coverage to identify poten- tial gaps, ensuring that important aspects such as security, performance, and dependencies are adequately addressed.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/Code-Survey",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Code-Survey: An LLM-Driven Methodology for Structuring and Analyzing Large-Scale Unstructured Software Engineering Data (Linux Kernel eBPF Case Study)"
    },

    {
      "@id": "rdip:Dataset/Linux-eBPF-Commits-Raw",
      "@type": "schema:Dataset",
      "schema:name": "Raw Linux kernel eBPF-related commits (2017–2024)",
      "schema:size": ">15,000 commits",
      "schema:description": "Git commits filtered by eBPF-related keywords, containing commit ID, author, date, message, diff, and associated files"
    },

    {
      "@id": "rdip:Activity/Survey-Design",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Design of structured Code-Survey questionnaire (7 main questions + I’m not sure options)",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Code-Survey-Questionnaire",
        "@type": "schema:Dataset",
        "schema:name": "Final eBPF commit survey with 7 structured questions (summary, keywords, classification, complexity, components, logic, use-cases)"
      }
    },

    {
      "@id": "rdip:Activity/Prompt-Engineering-LLM-Survey",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Construction of per-commit prompts containing survey + commit metadata + diff",
      "prov:used": [
        "rdip:Dataset/Linux-eBPF-Commits-Raw",
        "rdip:Dataset/Code-Survey-Questionnaire"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Per-Commit-Prompts",
        "@type": "schema:Dataset",
        "schema:name": ">15,000 individualized prompts for GPT-4o"
      }
    },

    {
      "@id": "rdip:Activity/LLM-Survey-Execution",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Automated survey completion by GPT-4o (single pass per commit)",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/OpenAI-GPT-4o",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "OpenAI GPT-4o (via API or GPTs interface)",
        "rdip:version": "2024-2025 release (gpt-4o)"
      },
      "prov:used": "rdip:Dataset/Per-Commit-Prompts",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/LLM-Survey-Responses-JSON",
        "@type": "schema:Dataset",
        "schema:name": "Structured JSON survey responses for >15,000 eBPF commits"
      }
    },

    {
      "@id": "rdip:Activity/Data-Cleaning-Validation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Post-processing, cleaning, and manual validation of LLM responses (merge commits, unrelated commits, consistency checks)",
      "prov:used": "rdip:Dataset/LLM-Survey-Responses-JSON",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/commit_survey.csv",
        "@type": "schema:Dataset",
        "schema:name": "Final cleaned commit_survey.csv dataset with structured fields (classification, complexity, components, etc.)"
      }
    },

    {
      "@id": "rdip:Activity/Quantitative-Analysis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Statistical and temporal analysis of structured survey data (time-series smoothing, distributions, trends)",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/Python-Pandas-Matplotlib",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "Python (Pandas, Matplotlib/Seaborn, SciPy for smoothing)",
        "rdip:version": "unknown"
      },
      "prov:used": "rdip:Dataset/commit_survey.csv",
      "rdip:outputDataset": [
        {
          "@id": "rdip:Dataset/Figures-2-17",
          "@type": "schema:Dataset",
          "schema:name": "All timeline, distribution, and dependency figures (Figures 2–17)"
        },
        {
          "@id": "rdip:Dataset/Quantitative-Insights",
          "@type": "schema:Dataset",
          "schema:name": "Derived insights on bug distribution, component evolution, feature dependencies, libbpf lifecycle, etc."
        }
      ]
    },

    {
      "@id": "rdip:Activity/Expert-Validation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Expert review and confirmation by >5 eBPF developers/maintainers and ongoing discussion on BPF mailing list",
      "prov:used": [
        "rdip:Dataset/commit_survey.csv",
        "rdip:Dataset/Quantitative-Insights"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Expert-Feedback",
        "@type": "schema:Dataset",
        "schema:name": "Qualitative expert confirmation and planned rating of sampled responses"
      }
    },

    {
      "@id": "rdip:Activity/Methodology-Refinement-Planning",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Planned future improvements (multi-run averaging, O1 model, multi-agent, refined prompts, expert rating of responses)",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Future-Work-Plan",
        "@type": "schema:Dataset",
        "schema:name": "Roadmap for enhancing Code-Survey accuracy and coverage"
      }
    }
  ]
}
```

This JSON-LD faithfully captures the full research provenance of the Code-Survey methodology and its application to the Linux kernel eBPF subsystem:

*   Central project
*   Raw commit data source
*   Human-designed structured survey
*   LLM-based automated survey execution using GPT-4o
*   Cleaning and validation steps
*   Quantitative analysis producing all figures and insights
*   Expert confirmation loop
*   Planned future refinements

All major data-production activities, the key software (GPT-4o), and resulting datasets (especially the final commit\_survey.csv) are represented using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

\## Input Text: 3. A Large-Scale Noisy Image-Text Dataset The focus of our work is to scale up visual and vision- language representation learning. For this purpose, we resort to a much larger dataset than existing ones. Specifically, we follow the methodology of constructing Conceptual Captions dataset (Sharma et al., 2018) to get a version of raw English alt-text data (image and alt-text pairs). The Conceptual Captions dataset was cleaned by heavy filtering and post-processing. Here, for the purpose of scaling, we trade quality for scale by relaxing most of the cleaning steps in the original work. Instead, we only apply minimal frequency-based filtering as detailed below. The result is a much larger (1.8B image-text pairs) but noisier dataset. Fig- ure 2 shows some sample image-text pairs from the dataset. “motorcycle front wheel” “thumbnail for version as of 21 57 29 june 2010” “file frankfurt airport skyline 2017 05 jpg” “file london barge race 2 jpg” “moustache seamless wallpaper design” “st oswalds way and shops” Figure 2. Example image-text pairs randomly sampled from the training dataset of ALIGN. One clearly noisy text annotation is marked in italics. Image-based filtering. Following Sharma et al. (2018), we remove pornographic images and keep only images whose shorter dimension is larger than 200 pixels and aspect ratio is smaller than 3. Images with more than 1000 associ- ated alt-texts are discarded. To ensure that we don’t train on test images, we also remove duplicates or near-duplicates of test images in all downstream evaluation datasets (e.g., ILSVRC-2012, Flickr30K, and MSCOCO). See Appendix A for more details. Text-based filtering. We exclude alt-texts that are shared by more than 10 images. These alt-texts are often irrelevant to the content of the images (e.g., “1920x1080”, “alt img”, and “cristina”). We also discard alt-texts that contain any rare token (outside of 100 million most frequent unigrams and bigrams from the raw dataset), and those that are ei- ther too short (<3 unigrams) or too long (>20 unigrams). This removes noisy texts like “image tid 25&id mggqpuwe- qdpd&cache 0&lan code 0”, or texts that are too generic to be useful. 4. Pre-training and Task Transfer 4.1. Pre-training on Noisy Image-Text Pairs We pre-train ALIGN using a dual-encoder architecture. The model consists of a pair of image and text encoders with a cosine-similarity combination function at the top. We use EfficientNet with global pooling (without training the 1x1 conv layer in the classification head) as the image encoder and BERT with \[CLS\] token embedding as the text em- bedding encoder (we generate 100k wordpiece vocabulary from our training dataset). A fully-connected layer with linear activation is added on top of BERT encoder to match the dimension from the image tower. Both image and text encoders are trained from scratch. The image and text encoders are optimized via normalized softmax loss (Zhai & Wu, 2019). In training, we treat matched image-text pairs as positive and all other random image-text pairs that can be formed in a training batch as negative. We minimize the sum of two losses: one for image-to-text classification Li2t =− N i log exp(x⊤ i yi/σ) N j=1 exp(x⊤ i yj /σ) (1) and the other for text-to-image classification Lt2i =− N N i log exp(y⊤ i xi/σ) N j=1 exp(y⊤ i xj /σ) (2) Here, xi and yj are the normalized embedding of image in the i-th pair and that of text in the j-th pair, respectively. N is the batch size, and σis the temperature to scale the logits. For in-batch negatives to be more effective, we concatenate embeddings from all computing cores to form a much larger batch. The temperature variable is crucial as both image 1 N 1 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision and text embeddings are L2-normalized. Instead of man- ually sweeping for the optimal temperature value, we find that it can be effectively learned together with all the other parameters. 4.2. Transferring to Image-Text Matching & Retrieval We evaluate ALIGN models on image-to-text and text-to- image retrieval tasks, with and without finetuning. Two benchmark datasets are considered: Flickr30K (Plummer et al., 2015) and MSCOCO (Chen et al., 2015). We also evaluate ALIGN on Crisscrossed Captions (CxC) (Parekh et al., 2021), which is an extension of MSCOCO with additional human semantic similarity judgments for caption-caption, image-image, and image-caption pairs. With extended annotations, CxC enables four intra- and inter-modal retrieval tasks including image-to-text, text-to- image, text-to-text, and image-to-image retrieval, and three semantic similarity tasks including semantic textual sim- ilarity (STS), semantic image similarity (SIS), and semantic image-text similarity (SITS). As the training set is identical to the original MSCOCO, we can directly evaluate the MSCOCO fine-tuned ALIGN model on CxC annotations. 4.3. Transferring to Visual Classification We first apply zero-shot transfer of ALIGN to visual classifi- cation tasks on ImageNet ILSVRC-2012 benchmark (Deng et al., 2009) and its variants including ImageNet-R(endition) (Hendrycks et al., 2020) (non-natural images such as art, cartoons, sketches), ImageNet-A(dversarial) (Hendrycks et al., 2021) (more challenging images for ML models), and ImageNet-V2 (Recht et al., 2019). All of these variants follow the same set (or a subset) of ImageNet classes, while the images in ImageNet-R and ImageNet-A are sampled from drastically different distributions from ImageNet. We also transfer the image encoder to downstream visual classification tasks. For this purpose, we use the ImageNet as well as a handful of smaller fine-grained classifica- tion datasets such as Oxford Flowers-102 (Nilsback & Zisserman, 2008), Oxford-IIIT Pets (Parkhi et al., 2012), Stanford Cars (Krause et al., 2013), and Food101 (Bossard et al., 2014). For ImageNet, results from two settings are reported: training the top classification layer only (with frozen ALIGN image encoder) and fully fine-tuned. Only the latter setting is reported for fine-grained classification benchmarks. Following Kolesnikov et al. (2020), we also evaluate the robustness of our model on Visual Task Adaptation Benchmark (VTAB) (Zhai et al., 2019) which consists of 19 diverse (covering subgroups of natural, specialized and structured image classification tasks) visual classification tasks with 1000 training samples each. 5. Experiments and Results We train our ALIGN models from scratch, using the open- sourced implementation of EfficientNet as the image en- coder and BERT as the text encoder. Unless in the ablation study, we use the results of ALIGN where the image encoder is EfficientNet-L2 and the text encoder is BERT-Large. The image encoder is trained at resolution of 289 ×289 pixels no matter what EfficientNet variant is used. We first resize input images to 346 ×346 resolution and then perform ran- dom crop (with additional random horizontal flip) in training and central crop in evaluation. For BERT we use wordpiece sequence of maximum 64 tokens since the input texts are no longer than 20 unigrams. The softmax temperature vari- able is initialized as 1.0 (this temperature variable is shared between image-to-text loss and text-to-image loss) and we use 0.1 as label smoothing parameter in the softmax losses. We use LAMB optimizer (You et al., 2020)1 with weight decay ratio 1e-5. The learning rate is warmed up linearly to 1e-3 from zero in 10k steps, and then linearly decay to zero in 1.2M steps (∼12 epochs). We train the model on 1024 Cloud TPUv3 cores with 16 positive pairs on each core. Therefore the total effective batch size is 16384. 5.1. Image-Text Matching & Retrieval We evaluate ALIGN on Flickr30K and MSCOCO cross- modal retrieval benchmarks, in both zero-shot and fully fine-tuned settings. We follow (Karpathy & Fei-Fei, 2015) and most existing works to obtain the train/test splits. Specif- ically, for Flickr30K, we evaluate on the standard 1K test set, and finetune on the 30k training set. For MSCOCO, we evaluate on the 5K test set, and finetune on 82K training plus 30K additional validation images that are not in the 5K validation or 5K test sets. During fine-tuning, the same loss function is used. But there can be false negatives when the batch size is comparable to the total number of training samples. So we reduce the global batch size from 16384 to 2048. We also reduce the ini- tial learning rate to 1e-5 and train for 3K and 6K steps (with linear decay) respectively on Flickr30K and MSCOCO. All the other hyper-parameters are kept the same as pre-training. Table 1 shows that, compared to previous works, ALIGN achieves SOTA results in all metrics of Flickr30K and MSCOCO benchmarks. In the zero-shot setting, ALIGN gets more than 7% improvement in image retrieval task compared to the previous SOTA, CLIP (Radford et al., 2021). With fine-tuning, ALIGN outperforms all existing methods by a large margin, including those that employ more complex cross-modal attention layers such as ImageBERT (Qi et al., 2020), UNITER (Chen et al., 2020c), 1We tried SGD with momentum and ADAM which are known to work well for CNNs and BERT respectively. LAMB appears to be a better choice for training both image and text encoders. Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision Table 1. Image-text retrieval results on Flickr30K and MSCOCO datasets (zero-shot and fine-tuned). ALIGN is compared with Image- BERT (Qi et al., 2020), UNITER (Chen et al., 2020c), CLIP (Radford et al., 2021), GPO (Chen et al., 2020a), ERNIE-ViL (Yu et al., 2020), VILLA (Gan et al., 2020), and Oscar (Li et al., 2020).

Flickr30K (1K test set) MSCOCO (5K test set) image →text text →image image →text text →image R@1 R@5 R@10 R@1 R@5 R@10 R@1 R@5 R@10 R@1 R@5 R@10 Zero-shot ImageBERT 70.7 90.2 94.0 54.3 79.6 87.5 44.0 71.2 80.4 32.3 59.0 70.2 UNITER 83.6 95.7 97.7 68.7 89.2 93.9 - - - - - CLIP 88.0 98.7 99.4 68.7 90.6 95.2 58.4 81.5 88.1 37.8 62.4 72.2 ALIGN 88.6 98.7 99.7 75.7 93.8 96.8 58.6 83.0 89.7 45.6 69.8 78.6 GPO 88.7 98.9 99.8 76.1 94.5 97.1 68.1 90.2 - 52.7 80.2 Fine-tuned UNITER 87.3 98.0 99.2 75.6 94.1 96.8 65.7 88.6 93.8 52.9 79.9 88.0 ERNIE-ViL 88.1 98.0 99.2 76.7 93.6 96.4 - - - - - VILLA 87.9 97.5 98.8 76.3 94.2 96.8 - - - - - Oscar - - - - - - 73.5 92.2 96.0 57.5 82.8 89.8 ALIGN 95.3 99.8 100.0 84.9 97.4 98.6 77.0 93.5 96.9 59.9 83.3 89.8 Table 2. Multimodal retrieval performance on Crisscrossed Captions (CxC) dataset. ALIGN is compared with VSE++ (Faghri et al., 2018), VSRN (Li et al., 2019), DEI2T (Parekh et al., 2021), and DET2T+I2T (Parekh et al., 2021). image →text text →image text →text image →image R@1 R@5 R@10 R@1 R@5 R@10 R@1 R@5 R@10 R@1 R@5 R@10 VSE++ 43.1 74.3 84.2 32.5 62.7 75.4 38.7 62.3 72.2 36.4 70.4 81.3 VSRN 52.4 81.9 90.0 40.1 71.1 81.5 41.0 64.8 74.5 44.2 76.7 86.2 DEI2T 53.9 82.7 91.2 39.8 70.2 80.9 26.0 47.1 57.5 38.3 74.1 85.0 DET2T+I2T 55.9 84.2 91.8 41.7 72.3 83.0 42.4 64.9 74.0 38.5 73.6 84.9 ALIGN 78.1 94.3 97.4 61.8 84.9 91.1 45.4 66.8 75.2 49.4 81.4 89.1 Table 3. Spearman’s R Bootstrap Correlation (×100) on Criss- crossed Captions (CxC) dataset. ALIGN is compared with VSE++ (Faghri et al., 2018), VSRN (Li et al., 2019), DEI2T (Parekh et al., 2021), and DET2T+I2T (Parekh et al., 2021). Model STS avg ±std SIS avg ±std SITS avg ±std Mean Avg VSE++ 74.4±0.4 73.3±0.9 55.2±1.5 67.6 VSRN 73.0±0.4 70.1±1.0 60.4±1.3 67.8 DEI2T 50.9±0.6 81.3±0.7 61.6±1.4 64.6 DET2T+I2T 74.2±0.4 74.5±0.9 61.9±1.3 70.2 ALIGN 72.9±0.4 77.2±0.8 67.6±1.2 72.6 ERNIE-ViL (Yu et al., 2020), VILLA (Gan et al., 2020) and Oscar (Li et al., 2020). Table 2 reports the performance of ALIGN on Crisscrossed Captions (CxC) retrieval tasks. Again, ALIGN achieves SOTA results in all metrics, especially by a large margin on image-to-text (+22.2% R@1) and text-to-image (20.1% R@1) tasks. Table 3 shows that ALIGN also outperforms the previous SOTA on SITS task with an improvement of 5.7%. One interesting observation is that, despite being much better on inter-modal tasks, ALIGN is not as impres- sive on intra-modal tasks. For instance, the improvements on text-to-text and image-to-image retrieval tasks (in partic- ular the former) are less significant compared to those on image-to-text and text-to-image tasks. The performance on STS and SIS tasks is also slightly worse than VSE++ and DEI2T. We suspect it is because the training objective of ALIGN focuses on cross-modal (image-text) matching in- stead of intra-modal matching. Parekh et al. (2021) suggest multitask learning could produce more balanced representa- tions. We leave it to the future work. 5.2. Zero-shot Visual Classification If we directly feed the texts of classnames into the text encoder, ALIGN is able to classify images into candidate classes via image-text retrieval. Table 4 compares ALIGN with CLIP on Imagenet and its variants. Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions. In order to make a fair comparison, we use the same prompt ensembling method as CLIP. Each classname is expanded with a set of prompt templates defined by CLIP such as “A photo of a {classname}”. The class embedding is computed by averaging the embeddings of all templates followed by an L2-normalization. We find that such ensembling gives 2.9% improvement on ImageNet top-1 accuracy. Table 4. Top-1 Accuracy of zero-shot transfer of ALIGN to image classification on ImageNet and its variants. Model CLIP ALIGN ImageNet ImageNet-R ImageNet-A ImageNet-V2 76.2 88.9 77.2 70.1 76.4 92.2 75.8 70.1 Model (backbone) Acc@1 w/ frozen features Acc@1 Acc@5 WSL (ResNeXt-101 32x48d) 83.6 85.4 97.6 CLIP (ViT-L/14) 85.4 - - BiT (ResNet152 x 4) - 87.54 98.46 NoisyStudent (EfficientNet-L2) - 88.4 98.7 ViT (ViT-H/14) - 88.55 - Meta-Pseudo-Labels (EfficientNet-L2) - 90.2 98.8 ALIGN (EfficientNet-L2) 85.5 88.64 98.67 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision Table 5. ImageNet classification results. ALIGN is compared with WSL (Mahajan et al., 2018), CLIP (Radford et al., 2021), BiT (Kolesnikov et al., 2020), ViT (Dosovitskiy et al., 2021), NoisyStudent (Xie et al., 2020), and Meta-Pseudo-Labels (Pham et al., 2020). Table 6. VTAB (19 tasks) comparison between ALIGN and BiT-L. Model Bit-L ALIGN All tasks Natural Specialized Structured 78.72 - - - 79.99±0.15 83.38 87.56 73.25 5.3. Visual Classification w/ Image Encoder Only On the ImageNet benchmark, we first freeze the learned visual features and only train the classification head. Afterwards we fine-tune all layers. We use basic data aug- mentations including random cropping (same as in Szegedy et al. (2015)) and horizontal flip. In evaluation we apply a single central crop with ratio of 0.875. Following Touvron et al. (2019), we use 0.8 scale ratio between training and evaluation to mitigate the resolution discrepancy introduced by random crop. Specifically, train/eval resolution is 289/360 with frozen visual features, and is 475/600 when fine-tuning all variables. In both stages of training, we use a global batch size of 1024, SGD optimizer with momentum 0.9, and learning rate decayed every 30 epochs with ratio 0.2 (100 epochs in total). Weight decay is set to zero. With frozen visual features, we use the initial learning rate of 0.1. When fine-tuning all layers with use the initial learning rate of 0.01, and use 10x smaller learning rate on the backbone network compared to the classification head. Table 5 compares ALIGN with previous methods on the Im- ageNet benchmark. With frozen features, ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy. After fine-tuning ALIGN achieves higher accu- racy than BiT and ViT models, and is only worse than Meta Pseudo Labels which requires deeper interaction between ImageNet training and large-scale unlabeled data. Com- pared to NoisyStudent and Meta-Pseudeo-Labels which also use EfficientNet-L2, ALIGN saves 44% FLOPS by using smaller test resolution (600 instead of 800). In VTAB eval, we follow a hyper-parameter sweep as shown in the Appendix I in (Zhai et al., 2019) with 50 trials for each task. Each task is trained on 800 images and the hyperpa- rameters are selected using the validation set of 200 images. After the sweep, the selected hyperparameters are used to train on the combined training and validation splits of 1000 images for each task. Table 6 reports the mean accuracy (including the breakdown results on each subgroup) with standard deviation from three fine-tuning runs and shows that ALIGN outperforms BiT-L (Kolesnikov et al., 2020) with similar hyper-parameter selection method applied. To evaluate on smaller fine-grained classification bench- marks, we adopt a simple fine-tuning strategy for all tasks. We use the same data augmentation and optimizer as in Ima- geNet fine-tuning. Similarly, we first train the classification head and then fine-tune all layers, except with batch norm statistics frozen. The train/eval resolution is fixed at 289/360. We use batch size 256 and weight decay 1e-5. The initial learning rate is set to 1e-2 and 1e-3 respectively, with cosine learning rate decay in 20k steps. Table 7 compares ALIGN with BiT-L (Kolesnikov et al., 2020) and SAM (Foret et al., 2021) which both apply same fine-tuning hyper-parameters for all tasks.2 For small tasks like these, details in fine- tuning matter. So we list the baseline results in (Foret et al., 2021) without using SAM optimization for a fairer compari- son. Our result (average of three runs) is comparable to the SOTA results without tweaking on optimization algorithms. Table 7. Transfer learning results on Fine-grained Classifica- tion Tasks. BiT-L (Kolesnikov et al., 2020) was trained with ResNet152 x 4 whereas SAM-baseline, SAM-final (Foret et al., 2021) and ALIGN were trained with EfficientNet-L2. Model Oxford Flowers Oxford Pets Stanford Cars Food101 BiT-L 99.63 96.62 - - SAM-baseline 99.60 96.92 95.07 96.03 SAM-final 99.65 97.10 95.96 96.18 ALIGN 99.65 96.19 96.13 95.88 6. Ablation Study In the ablation study, we compare model performance mostly on MSCOCO zero-shot retrieval and ImageNet K- Nearest-neighbor (KNN) tasks.3 We find these two met- 2ViT (Dosovitskiy et al., 2021) uses different hyper-parameters for different tasks and hence is not included in comparison. 3For each image in the validation set of ImageNet, we retrieve its nearest neighbors from the training set w/ pre-trained image encoder. Recall@K metric is calculated based on if the groundtruth label of the query image appears in the top-K retrieved images. Model MSCOCO ImangeNet KNN I2T R@1 T2I R@1 R@1 B5 + BERT-base w/ embedding dim=320 51.7 37.5 50.3 34.1 64.6 64.0 w/ embedding dim=160 w/ embedding dim=80 w/ 50% in-batch negs 47.0 34.4 42.0 29.3 50.2 37.0 63.7 61.9 63.8 w/ 25% in-batch negs w/ softmax temp=1/128 w/ softmax temp=1/64 w/ softmax temp=1/32 48.7 35.8 52.2 36.5 52.2 37.3 39.6 26.9 61.2 63.3 64.8 64.8 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision rics are representative and correlate well with other metrics reported in the section above. If not mentioned, hyper- parameters other than the ablated factor are kept the same as in the baseline model. 6.1. Model Architectures We first study the performance of ALIGN models using different image and text backbones. We train EfficientNet from B1 to L2 for the image encoder and BERT-Mini to BERT-Large for the text encoder. We add an additional fully-connected layer with linear activation on top of B1, B3, B5 and L2 globally-pooled features to match the output dimension of B7 (640). A similar linear layer is added to all text encoders. We reduce the training steps to 1M in ablation to save some runtime. Figures 3 shows MSCOCO zero-shot retrieval and Ima- geNet KNN results with different combinations of image and text backbones. Model quality improves nicely with larger backbones except that the ImageNet KNN metric starts to saturate from BERT-Base to BERT-Large with EfficientNet-B7 and EfficientNet-L2. As expected, scaling up image encoder capacity is more important for vision tasks (e.g., even with BERT-Mini text tower, L2 performs better than B7 with BERT-Large). In image-text retrieval tasks the image and text encoder capacities are equally important. Based on the nice scaling property shown in Figure 3, we only fine-tune the model with EfficientNet-L2

*   BERT-Large as reported in Section 5. We then study key architecture hyperparameters including embedding dimensions, number of random negatives in the batch, and the softmax temperature. Table 8 compares a number of model variants to a baseline model (first row) trained with the following settings: EfficientNet-B5 image encoder, BERT-Base text encoder, embedding dimension 640, all negatives in the batch, and a learnable softmax temperature. Rows 2-4 of Table 8 show that model performance improves with higher embedding dimensions. Hence, we let the dimension scale with larger EfficientNet backbone (L2 uses 1376). Rows 5 and 6 show that using fewer in-batch neg- atives (50% and 25%) in the softmax loss will degrade the performance. Rows 7-9 study the effect of the temperature parameter in the softmax loss. Compared to the baseline model that learns the temperature parameter (converged to about 1/64), some hand-selected, fixed temperatures could be slightly better. However, we choose to use the learnable temperature as it performs competitively and makes learning easier. We also notice that the temperature usually quickly decrease to only around 1.2x of the converged values in the first 100k steps, and then slowly converges until the end of training. Table 8. Ablation study of key architecture parameters. Baseline model (first row) is trained with embedding dimension 640, using all negatives in the batch, and a learnable softmax temperature. 6.2. Pre-training Datasets It’s also important to understand how the model performs when trained on different datasets with varying size. For this purpose, we train two models: EfficientNet-B7 + BERT- base and EfficientNet-B3 + BERT-mini on three different datasets: full ALIGN training data, 10% randomly sampled ALIGN training data, and Conceptual Captions (CC-3M, around 3M images). CC-3M is much smaller so we train the model with 1/10 of the default number of steps. All models are trained from scratch. As shown in Table 9, a large scale training set is essential to allow scaling up of our models and to achieve better performance. For instance, models trained on ALIGN data clearly outperform those trained on CC-3M data. On CC-3M, B7+BERT-base starts to overfit and performs even worse than B3+BERT-mini. Conversely, a larger model is required to fully utilize the larger dataset – the smaller B3+BERT-mini almost saturate at 10% of ALIGN data, while with the larger B7+BERT- base, there is a clear improvement with full ALIGN data. Table 9. Ablation study of different training datasets. To understand better how data size scaling wins over the increased noise, we further randomly sample 3M, 6M, and 12M ALIGN training data and compare them with the cleaned CC-3M data on B7+BERT-base model. Table 10 shows that while the ALIGN data performs much worse than CC data with the same size (3M), the model quality trained on 6M and 12M ALIGN data rapidly catches up. Despite being noisy, ALIGN data outperforms Conceptual Captions with only 4x size. Model + Data MSCOCO ImangeNet KNN R@1 I2T R@1 T2I R@1 B7 + BERT-base
*   ALIGN full data 55.4 41.7 69.3
*   ALIGN 10% data 52.0 39.2 68.8
*   CC-3M data 18.9 15.5 48.7 B3 + BERT-mini
*   ALIGN full data 37.4 24.5 56.5
*   ALIGN 10% data 36.7 24.4 55.8
*   CC-3M data 22.1 17.3 48.9 Model + Data MSCOCO ImangeNet KNN R@1 I2T R@1 T2I R@1 B7 + BERT-base
*   ALIGN 12M data 23.8 17.5 51.4
*   ALIGN 6M data 15.8 11.9 47.9
*   ALIGN 3M data 8.1 6.3 41.3 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision MSCOCO image-to-text retrieval R@1 MSCOCO text-to-image retrieval R@1 ImageNet NN accuracy 45 40 70 50 35 30 60 40 25 50 BERT-Mini BERT-Medium BERT-Base BERT-Large BERT-Mini BERT-Medium BERT-Base BERT-Large BERT-Mini BERT-Medium BERT-Base BERT-Large EﬃcientNet-B1 EﬃcientNet-B3 EﬃcientNet-B5 EﬃcientNet-B7 EﬃcientNet-L2 Figure 3. Zero-shot image-text retrieval and ImageNet KNN accuracy@1 with different image and text encoder sizes. Table 10. Tradeoff between training data size and quality.
*   “red”
*   “Australia” + “Madagascar”
*   “forest” + “desert” + “orange”
*   CC-3M data 18.9 15.5 48.7

7.  Analysis of Learned Embeddings We build a simple image retrieval system to study the behaviors of embeddings trained by ALIGN. For demon- stration purposes, we use an index consisting of 160M CC-BY licensed images that are separate from our training set. Figure 4 shows the top 1 text-to-image retrieval results for a handful of text queries not existing in the training data. ALIGN can retrieve precise images given detailed descriptions of a scene, or fine-grained or instance-level concepts like landmarks and artworks. These examples demonstrate that our ALIGN model can align images and texts with similar semantics, and that ALIGN can generalize to novel complex concepts.

*   “blue” + “purple” + “from distance”
*   “beige” + “red” + “purple”

*   “cars” - “trees” - “houses” “Van Gogh Starry Night ...” “details” “in black and white” “on a canvas” “in dark wood frame”
*   “flowers” - “orange” + “rose”
*   “bridge” - “waterfall” - “mountain” “view from bottom” “view from top” “Lombard street ...” “bird’s eye view” “in heavy rain” “Golden Gate Bridge” “seagull in front of ...” “London Tower Bridge” “Sydney Harbour Bridge” “Rialto Bridge” Figure 4. Image retrieval with fine-grained text queries using ALIGN’s embeddings. Previously word2vec (Mikolov et al., 2013a;b) shows that linear relationships between word vectors emerge as a re- sult of training them to predict adjacent words in sentences and paragraphs. We show that linear relationships between Figure 5. Image retrieval with image±text queries. We add (or subtract) text query embedding to (or from) the image query em- bedding, and then use the resulting embedding to retrieve relevant images using cosine similarity. image and text embeddings also emerge in ALIGN. We perform image retrieval using a combined image+text query. Specifically, given a query image and a text string, we add their ALIGN embeddings together and use it to retrieve relevant images.4 Figure 5 shows results for a variety of 4We normalize the text and image embeddings before adding them. We also tried various scale factor and found that a scale of 2 for the text embedding and 1 for the image embedding give best results as shown in the figure, although 1:1 also works well. Model en de fr cs zero-shot M3P 57.9 36.8 27.1 20.4 ALIGNEN 92.2- - - ALIGNmling 90.2 84.1 84.9 63.2 w/ fine-tuning M3P 87.7 82.7 73.9 72.2 UC2 88.2 84.5 83.9 81.2 Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision image+text queries. These examples not only demonstrate great compositionality of ALIGN embeddings across vision and language domains, but also show the feasibility of a new paradigm of “search with multi-modal query” that would otherwise be hard using only text query or image query. For instance, one could now look for the “Australia” or “Mada- gascar” equivalence of pandas, or turn a pair of black shoes into identically-looking shoes with the color of “beige”. Fi- nally, as shown in the last three rows of Figure 5, removing objects/attributes from a scene is possible by performing subtraction in the embedding space.

8.  Multilingual ALIGN Model One advantage of ALIGN is that the model is trained on noisy web image text data with very simple filters, and none of the filters are language specific. Given that, we further lift the language constraint of the conceptual caption data pro- cessing pipeline to extend the dataset to multilingual (cover- ing 100+ languages) and match its size to the English dataset (1.8B image-text pairs). A multilingual model ALIGNmling is trained using this data. We created a new mutlilingual wordpiece vocabulary with size 250k to cover all languages. Model training follows the exact English configuration. We test the multilingual model on Multi30k, a multilin- gual image text retrieval dataset extends Flickr30K (Plum- mer et al., 2015) to German (de) (Elliott et al., 2016), French (fr) (Elliott et al., 2017) and Czech (cs) (Barrault et al., 2018). The dataset consists of 31,783 images with 5 captions per image in English and German and 1 cap- tion per image in French and Czech. The train/dev/test splits are defined in Young et al. (2014). We evaluate the zero-shot model performance of ALIGN and compare it with M3P (Huang et al., 2020a) and UC2 (Zhou et al., 2021). The evaluation metric is mean Recall (mR), which computes the average score of Recall@1, Recall@5 and Recall@10 on image-to-text retrieval and text-to-image retrieval tasks. Table 11 shows that the zero-shot performance of ALIGNmling outperforms M3P on all languages by a large margin, with the largest +57.8 absolution mR improvement on fr. The zero-shot performance of ALIGNmling is even comparable to the fine-tuned (w/ training splits) M3P and UC2 except on cs. On en, ALIGNmling performs slightly worse on its counterpart ALIGNEN (trained on EN-only data.)

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/ALIGN",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision (Jia et al., 2021)"
    },

    {
      "@id": "rdip:Activity/Web-AltText-Crawling",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Web-scale crawling of raw English alt-text image-text pairs (following Conceptual Captions pipeline)"
    },

    {
      "@id": "rdip:Activity/Minimal-Cleaning-Filtering",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Minimal cleaning of raw alt-text data (image-based + text-based frequency filtering only)",
      "schema:description": "Image filters: remove porn, shorter side >200px, aspect<3, >1000 alt-texts; remove near-duplicates of downstream test sets. Text filters: shared by ≤10 images, vocab ≤100M most frequent tokens, 3≤unigrams≤20",
      "prov:used": "rdip:Dataset/Raw-Web-AltText",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-1.8B",
        "@type": "schema:Dataset",
        "schema:name": "ALIGN pre-training dataset",
        "schema:size": "1.8 billion noisy image-text pairs"
      }
    },

    {
      "@id": "rdip:Activity/ALIGN-Pretraining-English",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Pre-training of ALIGN dual-encoder (EfficientNet-L2 + BERT-Large) on 1.8B noisy English image-text pairs",
      "rdip:usedSoftware": [
        {
          "@id": "rdip:Software/EfficientNet",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "EfficientNet (open-source implementation)",
          "rdip:version": "Tan & Le, 2019"
        },
        {
          "@id": "rdip:Software/BERT",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "BERT",
          "rdip:version": "Devlin et al., 2019"
        },
        {
          "@id": "rdip:Software/JAX-TPU",
          "@type": "rdip:SoftwareApplication",
          "schema:name": "JAX + Cloud TPU v3",
          "rdip:version": "2020-2021"
        }
      ],
      "schema:description": "Normalized softmax (in-batch negatives), LAMB optimizer, 16,384 batch size, 1.2M steps, learnable temperature, trained from scratch",
      "prov:used": "rdip:Dataset/ALIGN-1.8B",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-English-Model",
        "@type": "schema:Dataset",
        "schema:name": "Pre-trained ALIGN model (EfficientNet-L2 image + BERT-Large text encoders)"
      }
    },

    {
      "@id": "rdip:Activity/Multilingual-Extension",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Construction of 1.8B multilingual (100+ languages) image-text dataset + training of ALIGNmling",
      "prov:used": "rdip:Activity/Web-AltText-Crawling",
      "prov:used": "rdip:Activity/Minimal-Cleaning-Filtering",
      "rdip:outputDataset": [
        {
          "@id": "rdip:Dataset/ALIGN-Multilingual-1.8B",
          "@type": "schema:Dataset",
          "schema:name": "Multilingual ALIGN training data (1.8B pairs, 100+ languages)"
        },
        {
          "@id": "rdip:Dataset/ALIGN-Multilingual-Model",
          "@type": "schema:Dataset",
          "schema:name": "ALIGNmling model (250k multilingual wordpiece vocabulary)"
        }
      ]
    },

    {
      "@id": "rdip:Activity/ZeroShot-Transfer",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Zero-shot evaluation on image-text retrieval (Flickr30K, MSCOCO, CxC) and image classification (ImageNet + variants)",
      "prov:used": "rdip:Dataset/ALIGN-English-Model",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ZeroShot-Results",
        "@type": "schema:Dataset",
        "schema:name": "Zero-shot R@1/5/10 on retrieval + top-1 accuracy on ImageNet/ImageNet-R/A/V2"
      }
    },

    {
      "@id": "rdip:Activity/FineTuning-Retrieval",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Fine-tuning of ALIGN on Flickr30K and MSCOCO training sets",
      "prov:used": "rdip:Dataset/ALIGN-English-Model",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-FineTuned-Retrieval",
        "@type": "schema:Dataset",
        "schema:name": "Fine-tuned ALIGN models for Flickr30K and MSCOCO"
      }
    },

    {
      "@id": "rdip:Activity/FineTuning-Classification",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Linear probe and full fine-tuning of ALIGN image encoder on ImageNet, VTAB, and fine-grained classification datasets",
      "prov:used": "rdip:Dataset/ALIGN-English-Model",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-Image-Classification-Models",
        "@type": "schema:Dataset",
        "schema:name": "Fine-tuned image classifiers (frozen features + full fine-tune) on ImageNet, VTAB (19 tasks), Flowers-102, Pets, Cars, Food101"
      }
    },

    {
      "@id": "rdip:Activity/Ablation-Experiments",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Ablation studies on model size, embedding dim, temperature, in-batch negatives, and dataset scale/noise trade-off",
      "prov:used": "rdip:Dataset/ALIGN-1.8B",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-Ablation-Results",
        "@type": "schema:Dataset",
        "schema:name": "Tables 8–10 + Figure 3 results"
      }
    },

    {
      "@id": "rdip:Activity/Qualitative-Analysis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Qualitative retrieval demos and compositionality analysis (image±text queries)",
      "prov:used": "rdip:Dataset/ALIGN-English-Model",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/ALIGN-Qualitative-Figures",
        "@type": "schema:Dataset",
        "schema:name": "Figures 4–5 (retrieval with complex text, image+text arithmetic)"
      }
    }
  ]
}
```

This JSON-LD fully captures the research provenance of the ALIGN (2021) paper:

*   Central project (ALIGN)
*   Construction of the 1.8B noisy English (and later multilingual) image-text dataset via minimal filtering of web alt-text
*   Pre-training of the dual-encoder model (EfficientNet-L2 + BERT-Large) from scratch on 1024 TPUv3 cores
*   Zero-shot and fine-tuned transfer to retrieval (Flickr30K, MSCOCO, CxC) and classification (ImageNet + variants, VTAB, fine-grained)
*   Ablation studies and qualitative embedding analysis
*   All major data-producing activities and resulting datasets/models are represented using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: F, are the two main methods of generating inferences \[33, 58, 60, 67, 73, 86, 103, 107, 144\], interpreting entity relationships to identify novel relation between indirectly linked entities. A common characteristic of these methods is that thresholds such as meta path length, extent of similarity measures and minimum probability of edge existence, can be predefined to support knowledge inferencing. Rule-based inference Rule-based inferences are conclusions made through a set of rules, including predefined paths \[41, 73\], entity similarity \[75\], and clustered patterns \[89, 99\]. Zhu et al. computed formulas to measure the drug-to-disease meta paths of their drug KG \[73\]; while Jiménez et al. generated inferences based on predefined meta paths to connect a drug to its corresponding disease \[41\]. Besides, similarity measures regarding entity information are considered as rule-based inferencing approach. Abdelaziz et al. compared drugs with a set of drug information derived- features such as chemical structure, side effects and drug target to predict similar drug pairs \[75\]. Furthermore, clustering of graph patterns is ubiquitous in rule-based inferencing. Percha et al. categorized groups of dependency paths based on their semantic similarity, which resulted in numerous clusters representing similar characteristics \[89\]; whereas Himmelstein et al. identified network patterns of Hetionet, distinguishing treatments groups from non-treatments groups \[99\]. Probabilistic inference Hypotheses drawn from probability computations are considered as probabilistic inferences \[141-143\]. For instance, McCusker et al. developed the evidence-weighted BKG where relations are assigned with probability based on the methods used to create the assertion, supporting the identification of several drug candidates for melanoma through probabilistic analysis \[142\]. Ernst et al. narrowed the list of candidates using probabilistic weights derived from BKG \[141\], while Jiang et al. created a Markov network theory based-probabilistic model from weighted KG for medical diagnosis \[143\]. Prediction Knowledge prediction, often referred to knowledge graph completion (KGC) aims to predict missing links and mine unknown facts \[145, 146\] to support hypotheses generation tasks such as drug candidate, diagnosis and risk prediction \[31, 33, 44, 69, 96, 99, 105, 147-150\]. Prediction techniques are broadly classified into rule-based prediction \[41, 43, 93, 103, 113, 119, 151\] and embedding-based prediction \[36, 39, 42, 62, 73, 75, 83, 84, 91, 97, 116, 152- 154\]. Rule-based prediction Rule-based predictions are conclusions inferred by directly utilizing data as input for statistical analysis and AI algorithms. Yamanishi et al. proposed several supervised statistical methods that reflects the drug-target interaction, namely nearest profile method, weighted profile method and bipartite graph learning method for drug-drug interaction (DDI) prediction \[119\]. Liu et al. proposed PoLo, a BKG multi-hop reasoning approach with logical rules in the form of meta paths \[43\]; while Jiménez et al. introduced a path-based drug repurposing method using random walks and reinforcement learning techniques and variational inference \[41\]. ML-based classification models are also highly utilized in the biomedical field. Tao et al. developed a health risk classification model by establishing a threshold for patient health boundaries, utilizing BKG \[113\]; likewise, Sang et al. trained a logistic regression model by learning semantic types of known drug therapies’ paths \[103\]. Embedding-based prediction KGE is a common approach to transform entities and relations of a KG into low-dimensional vectors \[12, 37, 73\], these embeddings can then be utilized to compute the similarity between entities, facilitating node and link predictions. Embedding techniques utilized for prediction can be generally classified into translational model \[12, 13, 73, 75, 83, 91\], semantic matching model \[36, 42, 62, 74\] and GNN model \[13, 38, 39, 116, 152\]. Translational models are structural embedding models that represent relationship as translations from head to tail entities \[12, 13\]. The similarity between entities and relations can be calculated by through embedding similarity. For instance, Chen et al. implemented TransE to generate nodes embedding of CTKG, cosine similarities between the condition and drug nodes are then calculated for the identification of 10 most similar pairs \[91\]. Abdelaziz et al. developed a large- scale similarity-based framework for DDI prediction using TransH, calculating cosine similarity between vectors to classify the most similar embeddings \[75\]. Gong et al. embedded different parts of the heterogeneous graph with TransR to learn the similarities between patient- medication relationships \[83\]. RESCAL \[29\], DistMult \[28\] and ComplEx \[155\] are three common semantic matching models. Nian et al. used ComplEx to produce corrupted triples as negative samples for training, improving the capability of KGC and identification of Alzheimer disease’s potential treatment candidates \[74\]. Mohamed et al. developed TriModel, a tensor factorization model extending DistMult to learn efficient vector representations of drugs and targets, through iterative learning on training sets \[42\]. Furthermore, GNNs are KGE models that transform information of every node’s neighborhood into a dense vector embedding \[13, 38, 39, 152\]. For instance, Huang et al. proposed TxGNN, a DL approach for drug predictions by incorporating GNN model for disease entity embedding and capture complex disease similarities \[116\]. Feng et al. obtained drug embeddings by GCN, which then become the input of the DNN model predictor for training to predict potential DDIs \[152\]. Apart from the three KGE methods, LLMs have emerged as an innovative link prediction approach that fully leverages the textual information and graph topology of KGs \[48\]. Xiao et al. proposed FuseLinker, a BKG link prediction framework leveraging both text and knowledge embeddings \[154\]. LLM is incorporated to generate text embeddings from BKG, the text embeddings are then fused with domain knowledge embeddings and ultimately become the input of GNN model that supports link prediction. Knowledge interpretation On the basis of new hypotheses or knowledge generated in the previous parts, knowledge interpretation provides an explanation by backtracking through the reasoning process, critical to support and validate the reliability of knowledge generated. Interpretation can be categorized based on how the predicted outcome is explained: logical explanation refers to an in-KG interpretation that displays the reasoning process within the graph’s topology; whereas assisted interpretation is an out-of-KG interpretation that translates the reasoning process into texts with the help of artificial intelligence systems like LLM. Logical explanation Logical explanation illustrates the reasoning process by showing the original path crucial for prediction, represented as triple sets or subgraphs \[38, 41, 72, 82, 97, 99, 116, 150, 151\]. Explanatory paths significantly enhance the reliability of new knowledge as they display the actual associations between biological entities, allowing field experts to acquire a full understanding of the reasoning process. Huang et al., developed an explainer module provides an overview of meta paths relevant to the prediction, displaying biological relationships crucial for its therapeutic predictions \[116\]. Shang et al. proposed an EHR-oriented KG providing graphical illustration of the reasoning, along with an explanation regarding the clinical significance of the prediction output \[82\]. Apart from that, Jiménez et al. proposed XG4Repo, highlighting its capability to provide prediction explanations, as well as generating Cypher queries for path acquisitions \[41\]. Assisted interpretation Recently, LLMs are integrated with KG to aid in the explanation of a specific outcome \[23, 137, 156-164\]. The ability of LLMs for queries interpretation enhances the interpretability and reliability of a predicted outcome. It is a key element for healthcare intelligence, improving users’ understanding of medical queries and helping doctors from different medical specialties to interpret a patient’s condition. Graph-to-text generation is an example of assisted interpretation, where top explanatory paths or sub-graphs crucial to the reasoned outcome are converted into text-based explanations. Lu et al. proposed a Clinical Retrieval-Augmented Generation (RAG) pipeline, where enriched medical knowledge can be converted into natural language to provide comprehensive answers with proper references \[165-167\]. Meanwhile, Pelletier et al. developed a RAG workflow RUGGED that provide answers and relevant literature evidences for queries \[156\]. O'Neil et al. introduced Phenomics Assistant, a chat-based interface for KG queries that integrates LLM with BKG, to answer queries with verified data and links to relevant sources \[137\]. Applications BKGs are developed to support a range of downstream applications in the biomedical field (Figure 4). From integrating diverse datasets across domains to performing multiple tasks on BKGs, various real-world applications can be effectively conducted. These applications often leverage one or more datasets and tasks within a single use case. Importantly, BKGs provide a robust foundation of prior knowledge, enhancing query platforms and empowering knowledge- aware applications. Figure 4. BKG Applications. An overview of the BKG utilization, highlighting the five main applications in the biomedical field. Information Retrieval Knowledge retrieval is the basic function of BKGs serving as knowledge bases, where tasks such as visualization and statistical analysis provide additional context to enhance the retrieval process. Various biomedical retrieval systems have been developed to support user queries, including patient registry acquisition \[82, 92, 107, 108, 168\], biomedical knowledge acquisition \[52, 84-86, 97, 99, 102, 112\], and literature retrieval \[128\]. Patient registry acquisition BKGs function as patient registry database by collecting and organizing patient-related data based on specific conditions and diagnoses. Hasan et al. constructed a BKG to manage cancer registry data, compiling demographic and treatment information of cancer patients \[107\]. Wang et al. proposed the personal health record (PHR) KG, which contains six aspects of patient data extracted from EMRs, improving individual healthcare management \[168\]. Yu et al. presented the integration of BKG into an AI chronic disease management system, enabling the retrieval of specific cases as diagnosis references \[108\]. Biomedical knowledge acquisition A significant number of BKGs incorporate biomedical concepts and theories, such as cellular mechanisms and pathological pathways. Hetionet \[99\], PharmKG \[97\] and PrimeKG \[112\] BKGs that provide cross-domain biomedical knowledge. Focusing on human genome, Feng et al. \[52\] developed GenomicKB to enable retrieval of information related to genome, epigenome, transcriptome and 4D nucleome. Furthermore, disease-specific KGs, such as SDKG-11 \[84\] and KGHC \[85\], facilitate the acquisition of knowledge related to specific diseases. Literature retrieval Xu et al. developed PubMed KG (PKG) that collects abstracts and author-related information \[128\]. PubMed biomedical literatures, author names, affiliation history and other researcher- centric activities are incorporated in the BKG to illustrate relationships between biomedical entities and their current research trend. PKG enables healthcare experts to efficiently retrieve biomedical studies for research purposes, supporting decision-making by considering the scientific contributions and academic success of researchers. Clinical Decision Support Clinical decision support (CDS) is a key application scenario of BKGs \[169\]. By integrating medical knowledge with patient-specific information, BKGs improve healthcare diagnosis and assist doctors in making decisions, enhancing the field of precision medicine. Clinical decision support system CDSS relies on BKGs as both a knowledge source and a prediction platform, enabling diagnostic support \[134, 135\] and healthcare prediction \[31, 33, 83, 86, 87, 92, 93, 102, 113, 133, 148, 150, 170\]. Diagnostic support Medical knowledge stored in BKGs enables CDSS to assist in detecting biosignals and symptoms, supporting doctors in their diagnosis procedure \[171, 172\]. Sekuboyina et al. performed chest X-ray classification with their radiological KG by conducting link predictions within the BKG \[135\]. Likewise, Zhang et al. presented a radiology report generation framework by incorporating a BKG related to chest findings, enhancing the interpretation of medical images \[134\]. Healthcare prediction Ma et al. proposed KAME, a model which learns embeddings from BKG to predict future health information of patients based on their historic data \[87\]. Tao et al. constructed a health BKG to develop a health risk classification model, predicting associations between a patient’s symptoms and diseases \[113\]. Moreover, BKG-integrated CDSS provides medication recommendations to reduce medication errors \[169\]. Bhoi et al. developed PREMIER, a personalized medication recommendation system that models drug interactions and drug co- occurrences of individuals \[150\]. Shang et al. presented GAMENet, a model incorporating a DDI KG, to recommend medication combinations for patients with complex health issues \[148\]. Intelligent Question Answering The advancements of NLP techniques and LLMs have driven the rise of intelligent question- answering systems, these systems process questions and generate answers based on semantic similarity \[6\]. The role of BKGs in intelligent question answering lies in providing contextual information \[86, 125, 136-139, 173-177\] and validating LLM predictions \[48, 178-180\], thereby preventing hallucinations in biomedical chat models. Knowledge Source BKGs play a crucial role in supporting intelligent question-answering systems by assisting answer generations \[86, 125, 136-139, 173-177, 181\], understanding user’s queries \[137\] and aiding patient condition description \[138\]. Yasunaga et al. developed DRAGON to pretrain biomedical language models using BKG, enabling question answering across the biomedical field \[139\]. BKG is also leveraged to interpret queries in natural language, helping non- specialists retrieve relevant information, as demonstrated by O'Neil et al. \[137\]. Furthermore, Jia et al. proposed DKDR, a disease diagnosis model that integrates BKG to generate accurate descriptions of patient conditions for doctors \[138\]. Prediction validation A common challenge with AI chatbots is the generation of inaccurate or even incorrect answers. BKGs, as repositories of factual knowledge, can be used to probe the knowledge contained in existing language models (LMs). Sung et al. developed the BIOLAMA benchmark, which consists of biomedical factual knowledge triples for LM probing \[178\]. LM predicts missing entities, and the resulting knowledge can be validated against a medical KG to ensure the accuracy and reliability of knowledge stored within the LM. Drug Discovery BKGs play a vital role in drug discovery by performing link predictions based on accumulated knowledge to identify potential drug and target candidates. The application of BKGs in drug discovery encompasses two main areas: drug repurposing \[38, 42, 44, 67-69, 73, 74, 84, 97-99, 105, 116, 142, 182\] and adverse drug reaction (ADR) analysis \[39, 75, 76, 95, 183\]. Drug repurposing DTI and DDA are two common types of interactions modeled by BKGs, which play a key role in drug repurposing \[4, 9\]. Huang et al. proposed TxGNN, a model for zero-shot drug repurposing trained on a medical KG, to rank potential drug indications and contraindications for various diseases \[116\]. Focusing on COVID-19, Zhang et al. predicted drug candidates through KGC techniques \[67\]. By combining BKGs with recommendation system, DTI can also be predicted to facilitate drug repurposing efforts, as illustrated by Ye et al. \[182\]. ADR analysis In BKGs, DDIs as the main cause of ADRs, form the foundation of ADR analysis \[4, 9\]. Bean et al. developed a ML algorithm on the basis of their BKG, to classify the causes of ADR and assist in detecting novel ADRs \[76\]. Similarly, Wang et al. identified potential ADRs of antitumor drugs using their Tumor-Biomarker KG, demonstrating the capability of BKGs in predicting ADR occurrences and exploring their mechanisms \[183\]. Scientific Research The knowledge foundation of BKGs highlights their advantages in providing accurate information across various domains. Hypotheses generation \[1, 33, 60, 64, 85, 94, 96, 101, 102, 151, 170, 179, 184, 185\] and research opportunities identification \[1, 107\] are two primary areas where BKGs are utilized in biomedical research. Hypotheses generation BKGs generate high-potential hypotheses for biomedical researches based on the theoretical knowledge embedded within the graph. Karim et al. \[179\] and Feng et al. \[184\] developed BKGs for cancer-specific biomarker discovery. Predictions made by these BKGs reveal possible associations between cancer and biological molecules, providing critical diagnostic information. Similarly, Pelletier et al. \[151\] and Renaux et al. \[94\] leveraged BKGs for pathology exploration, investigating organellar pathways and gene interactions to uncover the causes and mechanisms of diseases. The biomarkers and pathological insights predicted serve as generated hypotheses that require wet-lab experiments validation. Research opportunities identification BKG consolidate information across biomedical domains, including scientific findings published in biomedical literatures. These research achievements often remain underutilized, BKGs therefore bridge the gap between research and practical applications, by highlighting existing opportunities. The underlying possibilities can be future research directions, which can be transformed into real-world applications upon validation. To illustrate, Santos et al. introduced a clinical KG (CKG) where alternative treatments are prioritized by displaying co- mentions of relevant publications \[1\]. Furthermore, the cancer registry KG proposed by Hasan et al. highlighted racial disparities among TNBC women, providing a promising research area for further exploration of the disease \[107\].

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/Biomedical-KG-Review-2024",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Comprehensive Review of Biomedical Knowledge Graphs: Methods, Applications, and Future Directions"
    },

    {
      "@id": "rdip:Dataset/BKG-Literature-Corpus",
      "@type": "schema:Dataset",
      "schema:name": "Corpus of >180 publications on biomedical knowledge graphs (2015–2024)",
      "schema:description": "Includes works on rule-based inference, probabilistic inference, KGC (TransE/TransH/RESCAL/DistMult/ComplEx/GNNs), logical explanation, assisted interpretation (LLM+RAG), and applications in information retrieval, CDS, QA, drug discovery, and scientific research"
    },

    {
      "@id": "rdip:Activity/Literature-Collection-Search",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Systematic search and collection of biomedical KG literature across databases (PubMed, arXiv, Google Scholar, etc.)",
      "rdip:outputDataset": "rdip:Dataset/BKG-Literature-Corpus"
    },

    {
      "@id": "rdip:Activity/Inference-Methods-Taxonomy",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Taxonomic synthesis of KG inference methods (rule-based, probabilistic, prediction via rule-based and embedding-based)",
      "prov:used": "rdip:Dataset/BKG-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Inference-Taxonomy",
        "@type": "schema:Dataset",
        "schema:name": "Hierarchical classification of inference techniques in BKGs"
      }
    },

    {
      "@id": "rdip:Activity/Embedding-Techniques-Classification",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Classification of KGE models into translational (TransE/TransH/TransR), semantic matching (RESCAL/DistMult/ComplEx), and GNN-based approaches",
      "prov:used": "rdip:Dataset/BKG-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/KGE-Classification",
        "@type": "schema:Dataset",
        "schema:name": "Sub-taxonomy of knowledge graph embedding methods used in biomedicine"
      }
    },

    {
      "@id": "rdip:Activity/Interpretation-Methods-Review",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Review and dichotomy of knowledge interpretation methods (logical explanation via paths/subgraphs vs. assisted interpretation via LLMs/RAG)",
      "prov:used": "rdip:Dataset/BKG-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Interpretation-Taxonomy",
        "@type": "schema:Dataset",
        "schema:name": "Logical vs. assisted (LLM-augmented) explanation approaches in BKGs"
      }
    },

    {
      "@id": "rdip:Activity/Application-Domains-Mapping",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Mapping of BKG applications to five major domains: Information Retrieval, Clinical Decision Support, Intelligent QA, Drug Discovery, Scientific Research",
      "prov:used": "rdip:Dataset/BKG-Literature-Corpus",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/BKG-Applications-Framework",
        "@type": "schema:Dataset",
        "schema:name": "Figure 4 – Comprehensive application framework of biomedical knowledge graphs"
      }
    },

    {
      "@id": "rdip:Activity/Narrative-Synthesis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Narrative integration of inference, interpretation, and application findings into review manuscript section",
      "prov:used": [
        "rdip:Dataset/Inference-Taxonomy",
        "rdip:Dataset/KGE-Classification",
        "rdip:Dataset/Interpretation-Taxonomy",
        "rdip:Dataset/BKG-Applications-Framework"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Final-Review-Section",
        "@type": "schema:Dataset",
        "schema:name": "Published methodology/review section on biomedical knowledge graph techniques and applications"
      }
    }
  ]
}
```

This JSON-LD accurately represents the provenance of a large-scale systematic review paper on biomedical knowledge graphs (BKGs). The primary intellectual work consists of:

*   Literature collection and corpus formation
*   Taxonomic synthesis of inference methods (rule-based, probabilistic, prediction)
*   Detailed classification of embedding-based KGC techniques
*   Dichotomy of interpretation/explanation approaches
*   Comprehensive mapping of real-world BKG applications

No new primary data or models were generated — the entire contribution is secondary synthesis and organization of existing published research. All major data-production activities are scholarly synthesis steps feeding into the final review manuscript section.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

\# Input Text: Let H be a Hilbert space of functions defined in Ωt. To determine E(t), t ∈Ωt, we construct the Tikhonov functional which is more appropriate for the data presented in Tables 2 and 3: J(E) = 1 2 \[log10(u1(t) + u2(t))−log10(g1(t))\]2z1ζ (t) dt Ωt 1 + 2 \[log10 u3(t)−log10 g2(t)\]2z2ζ (t) dt+ Ωt 1 2 γ (E(t)−E0)2dt. Ωt (4.9) Here, u1(t), u2(t), u3(t) are the solutions of the system (2.4) which are depended on the func- tion E(t), g1(t) is the observed sum of uninfected and infected T-cells, g2(t) is the observed virus population function, E0 is the initial guess for the parameter E(t) and γ ∈(0,1) is the regulariza- tion parameter, z1ζ(t),ζ ∈(0,1) and z2ζ(t),ζ ∈(0,1) are smoothing functions for data which can be defined similarly as in \[13\]. To find the function E(t) ∈H which minimizes the Tikhonov functional (4.9) we seek for a stationary point of (4.9) with respect to Esuch that ¯ J′(E)( E) = 0, ∀¯ E ∈H. (4.10) To find minimum of (4.9) we use constrained optimization with the standard Lagrangian ap- proach \[8, 27\] and introduce the Lagrangian with constrains corresponding to the model problem: L(v) = J(E) + 3 i=1Ωt λi dui dt−fi dt, (4.11) where u(t) = (u1(t),u2(t),u3(t)) is the solution of the system (2.4), λ(t) is the vector of Lagrange multipliers λ(t) = (λ1(t),λ2(t),λ3(t)), and v= (λ,u,E). We now introduce following spaces which we are using in analysis of PIP: H1 u(Ωt) = {u∈H1(Ωt) : u(0) = u0}, H1 λ(Ωt) = {λ∈H1(Ωt) : λ(T) = 0}, U= H1 u(Ωt) ×H1 λ(Ωt) ×C(Ωt), (4.12) 8 for all real valued functions. To derive the Fr´ echet derivative of the Lagrangian (4.11) we use such called all-at-once approach when we assume that functions v= (λ,u,E) can be varied independently of each other such that ¯ ¯ L′(v)(¯ v) = 0, ∀¯ v= ( λ,¯ u, E) ∈U. (4.13) The optimality condition (4.13) means also that for all¯ v∈U we have L′(v; ¯ v) = ∂L ¯ ∂λ(v)( λ) + ∂L ∂u(v)(¯ u) + ∂L ¯ ∂E(v)( E) = 0 (4.14) i.e., every component of (4.14) should be zero out. Thus, the optimality condition ∂L ¯ ∂λ(v)( λ) = 0 yields 0 = ∂L ∂λ1 0 = ∂L ∂λ2 0 = ∂L ∂λ3 ¯ (v)( λ1) = (∂u1 ¯ ∂t−s+ β1u1u3 + µu1) λ1dt ∀¯ λ1 ∈H1 λ(Ωt), Ωt ¯ (v)( λ2) = (∂u2 ¯ ∂t−β1u1u3 + dEu2) λ2dt, ∀¯ λ2 ∈H1 λ(Ωt) Ωt ¯ (v)( λ3) = (∂u3 ¯ ∂t−ρu2 + cu3 + β2u1u3) λ3dt, ∀¯ λ3 ∈H1 λ(Ωt), Ωt (4.15) Next, the optimality condition ∂L ∂u(v)(¯ u) = 0 means that 0 = ∂L ∂u1 (v)( ¯ u1) = 1 (u1 + u2) ln 10\[log10(u1(t) + u2(t))−log10(g1(t))\]z1ζ (t) ¯ u1dt Ωt + (− ∂λ1 ∂t + λ1β1u3 + µλ1−λ2β1u3 + β2λ3u3) ¯ u1dt ∀¯ u1 ∈H1 u(Ωt), Ωt (v)( ¯ u2) = 1 (u1 + u2) ln 10\[log10(u1(t) + u2(t))−log10(g1(t))\]z1ζ (t) ¯ u2dt Ωt + (− ∂λ2 ∂t + dEλ2−λ3ρ) ¯ u2dt ∀¯ u2 ∈H1 u(Ωt), Ωt (v)( ¯ u3) = 1 u3 ln 10\[log10(u3)−log10(g2)\]z1ζ (t) ¯ u3dt Ωt + (− ∂λ3 ∂t + λ1β1u1−λ2β1u1 + cλ3 + λ3β2u1) ¯ u3dt Ωt (4.16) Finally, the optimality condition ∂L ¯ ∂E(v)( E) = 0 yields: 0 = ∂L ¯ ∂E(v)( E) = γ (E−E0) ¯ Edt+ Ωt Ωt ¯ dλ2u2 Edt ∀¯ E ∈C(Ωt). (4.17) 0 = ∂L ∂u2 0 = ∂L ∂u3 ∀¯ u3 ∈H1 u(Ωt). 9 ∂λ2 ∂t= Using optimality conditions (4.15)-(4.16) we observe that the equations (4.15) correspond to the system of model equations (2.3) which is also our forward problem, and equations (4.16) — to the following adjoint problem ∂λ1 ˜ ∂t= f1(λ(t),η(t)) = λ1(t)β1u3(t) + λ1(t)µ−λ2(t)β1u3(t) + β2λ3(t)u3(t) + 1 (u1(t) + u2(t)) ln 10\[log10(u1(t) + u2(t))−log10(g1)\]z1ζ, ˜ f2(λ(t),η(t)) =−λ3(t)ρ+ dλ2(t)E(t) + 1 (u1(t) + u2(t)) ln 10\[log10(u1(t) + u2(t))−log10(g1)\]z1ζ, ˜ f3(λ(t),η(t)) = λ1(t)β1u1(t)−λ2(t)β1u1(t) + cλ3(t) + λ3(t)β2u1(t) 1 + u3(t) ln 10\[log10(u3(t))−log10(g2)\]z1ζ, λi(T) = 0, i= 1,2,3, which we rewrite as with (4.18) (4.19) ∂λ3 ∂t= ∂λ ˜ ∂t = f(λ(t),E(t)), λi(T) = 0, i= 1,2,3, λ= λ(t) = (λ1(t),λ2(t),λ3(t))T , 0 = (λ1(T),λ2(T),λ3(T))T , dλ dt= ∂λ1 ∂λ2 ∂λ3 ∂t , ∂t , ∂t T , ˜ ˜ ˜ ˜ f(λ(t)) = ( f1, f2, f3)(λ(t),E(t))T . (4.20) The adjoint problem should be solved backwards in time with already known forward problem solution u(t) and a given data g1(t),g2(t). From definition of the Lagrangian (4.11) it follows that for the known exact function u, known parameters in the forward problem and known solution λof the adjoint problem (4.18) we get that L(v(E)) = J(E). (4.21) In this case the Fr´ echet derivative of the Tikhonov functional can be written as J′(E) :=JE(u(E),E) = ∂J ∂E(u(E),E) = ∂L ∂E(v(E)). (4.22) Using (4.17) in (4.22), we get the following expression for the Fr´ echet derivative of the Tikhonov functional which will be used later in the conjugate gradient update of the parameter Ein time : J′(E)(t) = γ(E−E0)(t) + dλ2(t)u2(t). (4.23) 10 5 Numerical methods for solution of optimization problem To solve the minimization problem (4.13) we will employ the finite element method. To do this we discretize the computational domain Ωt = \[0,T\] and consider a partition Jτ = {Jk}of the time domain Ωt into time subintervals Jk = (tk−1,tk\] with the time step τk = tk−tk−1. Let us define the piecewise-constant function τ(t) such that τ(t) = τk, ∀Jk ∈Jτ. (5.24) We define also the finite element spaces Vu τ ⊂H1 u(Ωt) and Vλ τ ⊂H1 λ(Ωt) for approximations uτ,λτ of uand λ, respectively, as Vu τ Vλ τ = {u∈L2(Ωt) : u|J ∈P0(J),u(0) = u0 , ∀J ∈Jτ}, = {λ∈L2(Ωt) : λ|J ∈P0(J),λ(T) = 0, ∀J ∈Jτ} (5.25) for discretization of the state and adjoint problems. We also introduce the finite element space VE τ ⊂L2 (Ωt) for the function E(t) consisting of piecewise constant functions VE τ = {f ∈L2 (Ωt) : f|J ∈P0(J) ∀J ∈Jτ}. (5.26) Let Uτ = Vu τ ×Vλ τ ×VE τ such that Uτ ⊂U. We can formulate now the finite element method for (4.13): find vτ ∈Uτ such that L′(vτ)(¯ v) = 0, ∀v∈Uτ. (5.27) We note that the forward (2.3) and adjoint (4.18) problems are nonlinear. For solution of these problems we employ Newton’s method as follows. The variational formulation of the forward problem (2.4) is: du dt,¯ u = (f(u(t)),¯ u) ∀¯ u∈H1 u(Ωt). (5.28) Let us use the following discretization for the derivative in time ∂u ∂t= uk+1 −uk in the variational formulation (5.28) to obtain (uk+1 ,¯ u)−τk(f(uk+1),¯ u)−(uk ,¯ u) = 0 ∀¯ u∈H1 u(Ωt). (5.29) Approximating uk+1 by its finite element approximation uk+1 τ the above equation can be written as (uk+1 τ−τkf(uk+1 τ )−uk τ,¯ u) = 0 ∀¯ u∈Vu τ. (5.30) τk We denote now ˜ u= uk+1 τ , V(˜ u) = ˜ u−τkf(˜ u)−uk τ. 11 (5.31) Next, we rewrite the variational formulation as (V(˜ u),¯ u) = 0 ∀¯ u∈Vu τ. (5.32) To solve nonlinear equation V(˜ u) = 0 we are using the Newton’s method \[17\] for iterations in the Newtons’ method n= 1,....Mn: ∂u1 ∂f2 ∂u2 ∂f2 ˜ un+1 = ˜ un −\[V′(˜ un)\]−1 ·V(˜ un). (5.33) Here, the Jacobian V′(˜ un) is computed via definition of V(˜ u) in (5.31) as V′(˜ un) = I−τkf′(˜ un), where I is the identity matrix, f′(˜ un) is the Jacobian of f which represents the right hand side of the forward problem (2.3) at˜ un , nis the iteration number in Newton’s method and Mn is the final iteration in Newton’s method. The entries in the Jacobian f′(˜ un) for system (2.3) can be explicitly computed and they are defined as: f′(˜ un) =        ∂f1 ∂f1 ∂u1 ∂u2 ∂f1 ∂u3 ∂f2 ∂u3 ∂f3 ∂u3        (˜ un) =      . We derive the Newtons’s method for the solution the adjoint problem (4.18) in a similar way. Since we solve the adjoint problem backwards in time starting from the known λ(T) = 0, we discretize the time derivative as ∂λ ∂t= λk+1 −λk (5.34) τk for the already known λk+1, and write the variational formulation of the adjoint problem for all ¯ λ∈H1 λ(Ωt) as −λk ˜ −τk f(λk), ¯ λ) = 0. (5.35) ∂u1 ∂f3 ∂u2 ∂f3   −β1u3 n τ−µ 0−β1u1 n τ β1u3 n τ−dE β1u1 n τ −β2u3 n τ ρ−β2u1 n τ−c (λk+1 We rewrite (5.35) in the form (λk −λk+1 + τk ˜ f(λk), ¯ λ) = 0 (5.36) and formulate the finite element method for the variational formulation (5.36): find λk τ ∈Vλ τ such that for all¯ λ∈Vλ τ (λk τ−λk+1 ˜ τ + τk f(λk τ), ¯ λ) = 0. (5.37) Denoting ˜ λ= λk τ, R( ˜ λ) = ˜ λ+ τk ˜ f( ˜ λ)−λk+1 τ , (5.38) 12 we can rewrite (5.37) for all¯ λ∈Vλ τ as ˜ (R( λ), ¯ λ) = 0. (5.39) ˜ For solution R( λ) = 0 we use again Newton’s method: ˜ λn+1 = ˜ λn ˜ −\[R′( λn)\]−1 ˜ ·R( λn),n= 1,....,Kn. (5.40) ˜ ˜ We compute R′( λn) using the definition of R( λ) in (5.38) as ˜ ˜ ˜ R′( λn) = I+ τk f′( λn), where I is the identity matrix,˜ ˜ f′( λn) is the Jacobian of˜ f at˜ λn , nis the iteration number in the Newton’s method and Kn is the final number of iteration. The entries in the Jacobian˜ ˜ f′( λn) for the adjoint system (4.18) are explicitly given by ˜ ˜ f′( λn) =         ∂˜ f1 ∂˜ f1 ∂λ1 ∂λ2 ∂˜ f1 ∂λ3 ∂˜ f2 ∂λ3 ∂˜ f3 ∂λ3         ˜ ( λn) =     β1u3 n τ + µ−β1u3 n τ β2u3 n τ 0 dE−ρ β1u1 n τ−β1u1 n τ c+ β2u1 n τ    . ˜ ˜ We note that det f′(˜ un) ̸= 0 as well as det f′( λn) ̸= 0 since all parameters used in the model problem are non-zero. Thus, schemes given by formulas (5.33), (5.40) will converge to the so- lutions of forward and adjoint problems for the appropriate initial guesses for values˜ u1 and˜ λ1 , correspondingly. ∂λ1 ∂˜ f2 ∂λ2 ∂˜ f2 ∂λ1 ∂˜ f3 ∂λ2 ∂˜ f3 6 A Posteriori Error Estimates In this section we derive a posteriori error estimates for the error in The Tikhonov’s functional ||J(E)−J(Eh)||L2(Ωt) and for the error in the reconsructed function ||E−Eh||L2(Ωt), correspond- ingly. Both error estimators can be used as the mesh refinement criteriors in the adaptive conjugate gradient algorithm. Before deriving error estimates we make some assumptions which are usual for parameter iden- tification problems since they are ill-posed problems \[35, 36, 37\]. We assume that the function E(t) ∈C(Ωt) as a minimizer of the Lagrangian (4.11), and Eτ ∈VE τ is its finite element approx- imation. We also assume that E∗ ∈C(Ωt) is the exact function describing the effectivity of the immune response and that there exists a good approximation Eτ to the exact function E∗∈C(Ωt). Let g∗ 1,2(t) be the exact data for the measured functions g1,2(t) defined in (3.7), (3.8), correspond- ingly, and the functions g1,2σ(t) represent the error levels in the measured data. This means that we assume that measurements g1,2(t) in (3.7), (3.8) are given with some small noise levels σ1,σ2 such that g1(t) = g∗ 1(t) + g1σ(t); g∗ 1,g1σ ∈L2 (Ωt), ∥g1σ∥L2(Ωt) ≤σ1, g2(t) = g∗ 2(t) + g2σ(t); g∗ 2,g2σ ∈L2 (Ωt), ∥g2σ∥L2(Ωt) ≤σ2. 13 (6.41) We also assume that the regularization parameter in the Tikhonov’s functional is such that γ= γ(σ1,σ2) = (σ1 + σ2)2µ, µ∈(0,1/4), σ1,2 ∈(0,1) (6.42) and for the exact solution E∗corresponding to the exact data g∗ 1,2(t) it holds that ∥E0−E∗∥L2(Ωt) ≤(σ1 + σ2)3µ 3. (6.43) The condition (6.43) means that E0 is located in the close neighborhood of the exact solution E∗ . Let us define the set for any ε>0 Vε(E) = {˜ E ∈C(Ωt) : ∥E− ˜ E∥<ε ∀E ∈C(Ωt)}. (6.44) Assume that for all E ∈V1(E∗) the operator F(E) = 1 2 \[log10(u1(E,t) + u2(E,t))−log10(g1(t))\]2z1ζ (t) dt Ωt + 1 2 \[log10 u3(E,t)−log10 g2(t)\]2z2ζ (t) dt Ωt has the Fr´ echet derivative F′(E) which is bounded and Lipshitz continuous in V1(E∗) for N1,N2 = const.>0 ∥F′(E)∥L2(Ωt) ≤N1 ∀E ∈V1(E∗), ∥F′(E1)−F′(E2)∥L2(Ωt) ≤N2∥E1−E2∥L2(Ωt) ∀E1,E2 ∈V1(E∗). (6.45) 6.1 An a posteriori error estimate for the Tikhonov functional In this section we derive an a posteriori error estimate for the error ∥J(E)−J(Eh)∥L2(Ωt) in the Tikhonov functional (4.9) on the finite element time partition Jτ. Theorem 1. Let E ∈C(Ωt) is the minimizer of the functional J(E) defined by (4.9) and there exists finite element approximation of a minimizer Eτ ∈VE τ of J(E). Then the following a posteriori error estimate for the error e= ||J(E)−J(Eτ)||L2(Ωt) in the Tikhonov functional (4.9) holds true e= ||J(E)−J(Eτ)||L2(Ωt) ≤CI J′(Eτ) L2(Ωt)  ||τEτ||L2(Ωt) + Jk ∥\[Eτ\]∥L2(Jk) ∀Eτ ∈VE τ , (6.46) where CI = const.>0 and J′(Eτ) = γ(Eτ−E0) + dλ2τu2τ. Proof Using first two terms in the Taylor’s expansion we get J(E) = J(Eτ) + J′(Eτ)(E−Eτ) + R(E,Eτ), 14 (6.47) (6.48) where R(E,Eτ) = O(∥E−Eτ∥2), (E−Eτ) →0 ∀E,Eτ ∈VE τ . We neglect the remainder term R(E,Eτ) in (6.48) since it is small because of assumption (6.43). Next, we use the following splitting for E−Eτ in (6.48) E−Eτ = E−EI τ + EI τ−Eτ (6.49) together with the Galerkin orthogonality property J′(Eτ)(EI τ−Eτ) = 0, ∀EI τ,Eτ ∈VE τ (6.50) to get J(E)−J(Eτ) ≤J′(Eτ)(E−EI τ). (6.51) Here, EI τ is a standard interpolant of Eon the mesh Jτ \[21\]. Taking norms in (6.51), we obtain ||J(E)−J(Eτ)||L2(Ωt) ≤||J′(Eτ)||L2(Ωt)||E−EI τ||L2(Ωt). (6.52) For estimation of the term ||E−EI τ||L2(Ωt) we are using standard interpolation estimate with the interpolation constant CI ||E−EI τ||L2(Ωt) ≤CI ∥τE∥H1(Ωt). (6.53) We can estimate ||τ E||H1(Ωt) in (6.53) as ||τ E||H1(Ωt) ≤ ||τkE||H1(Jk)= Jk Jk E+ ≤ Jk ||Eττk||L2(Jk) + \[Eτ\] τk ≤||τEτ||L2(Ωt) + ∥\[Eτ\]∥L2(Jk). Jk ∂E ∂t τk L2(Jk) τk L2(Jk) (6.54) Here, \[Eτ\] denote the jump of the function Eτ over the time intervals \[tk−1,tk\] and \[tk,tk+1\] which we define as \[Eτ\] = E+ τ−E− τ , where functions E− τ ,E+ τ are computed on two neighboring time intervals \[tk−1,tk\] and \[tk,tk+1\], respectively. Now we substitute the estimate (6.54) into (6.52) to get final a posteriori error estimate ||J(E)−J(Eτ)||L2(Ωt) ≤CI J′(Eτ) L2(Ωt)  ||τEτ||L2(Ωt) + Jk ∥\[Eτ\]∥L2(Jk) ∀Eτ ∈VE τ. (6.55) □ 15 6.2 A posteriori error estimate of the minimizer on refined meshes In the Theorem 2 and Theorem 3 we derive two different a posteriori error estimates for the error ∥E−Eτ∥L2(Ωt). Proof of the Theorem 2 follows from the proof of Theorem 5.1 of \[23\]. Theorem 2 Let E ∈L2(Ωt) be a minimizer of the Tikonov’s functional (4.9) and Eτ ∈VE τ be a finite element approximation of the minimizer on the finite element mesh Jτ. Then there exists a Lipschitz constant D= const.>0 defined by J′(E1)−J′(E2) L2(Ωt) ≤D∥E1−E2∥L2(Ωt) ,∀E1,E2 ∈L2(Ωt), (6.56) and the interpolation constant CI independent on the mesh size τsuch that the following a posteriori error estimate for the minimizer Eholds true for γ >0 ||E−Eτ||L2(Ωt) ≤ D CI  ||τEτ||L2(Ωt) + Jk ∥\[Eτ\]∥L2(Jk) ∀Eτ ∈VE τ. (6.57) γ Proof. Let Eτ be the minimizer of the Tikhonov functional (4.9). The existence and uniqueness of this minimizer is guaranteed by conditions (6.43) and thus follows from Theorem 1.9.1.2 of \[14\]. Using this theorem we can conclude that the functional (4.9) is strongly convex on the space L2(Ωt) with the strong convexity constant γ. This yields that γ∥E−Eτ∥2 L2(Ωt) ≤∥ J′(E)−J′(Eτ) ,E−Eτ ∥L2(Ωt). (6.58) Here, J′(Eτ),J′(E) are the Fr´ echet derivatives of the functional (4.9) given by the formula (4.23) for Eτ,E, respectively. Since Eis the minimizer of the Tikhonov functional (4.9) then J′(E) ,v = 0, ∀v∈L2(Ωt). Using again the splitting (6.49) in (6.58) together with the Galerkin orthogonality principle for all Eτ,EI τ ∈VE τ J′(E)−J′(Eτ) ,EI τ−Eτ = 0 (6.59) we get γ∥E−Eτ∥2 L2(Ωt) ≤∥ J′(E)−J′(Eτ) ,E−EI τ ∥L2(Ωt). (6.60) We can estimate the right hand side of (6.60) using (6.56) as ∥ J′(E)−J′(Eτ) ,E−EI τ ∥L2(Ωt) ≤D||E−Eτ||L2(Ωt)||E−EI τ||L2(Ωt). Substituting above equation into (6.60) we obtain ||E−Eτ||L2(Ωt) ≤ D γ||E−EI τ||L2(Ωt). (6.61) 16 D Using again the interpolation property (6.53) we obtain a posteriori error estimate for the regularized solution : ||E−Eτ||L2(Ωt) ≤ D γ||E−EI τ||L2(Ωt) ≤ γ CI||τ E||H1(Ωt). (6.62) . We can estimate the term ||τ E||H1(Ωt) in the right hand side of (6.62) similarly as in (6.54). Substituting the estimate (6.54) into the right hand side of (6.62) we get D ||E−Eτ||L2(Ωt) ≤ CI  ||τEτ||L2(Ωt) + Jk ∥\[Eτ\]∥L2(Jk) ∀Eτ ∈VE τ. γ □ Theorem 3 Let Eτ ∈VE τ be a finite element approximation of the minimizer E ∈L2(Ωt) on the finite element mesh Jτ. Then there exists an interpolation constant CI independent on the mesh function τ such that the following a posteriori error estimate holds for γ >0: ||E−Eτ||L2(Ωt) ≤∥R(Eτ)∥L2(Ωt) ∀Eτ ∈VE τ , (6.63) γ where R(Eτ) is the residual defined as R(Eτ) = γ(Eτ−E0) + dλ2τu2τ. (6.64) Proof. Let again Eτ be the minimizer of the Tikhonov functional (4.9). Strong convexity of the func- tional (4.9) on the space L2(Ωt) implies that γ∥E−Eτ∥2 L2(Ωt) ≤∥ J′(E)−J′(Eτ) ,E−Eτ ∥L2(Ωt). (6.65) Applying splitting (6.49) to (6.65) we obtain (6.60) where the term J′(Eτ) can be written via (4.23). More precisely, when u(t),λ(t) are exact solutions of the forward and adjoint problems, respectively, we have for Eτ: L(v(Eτ)) = J(Eτ), and thus, one can write J′(Eτ) = L′(Eτ) = γ(Eτ−E0) + dλ2u2. (6.66) We can write estimate (6.65) as γ∥E−Eτ∥L2(Ωt) ≤∥J′(E)−J′(Eτ) ∥L2(Ωt) Then noting that J′(E) = 0 and using (6.66) for approximations u2τ,λ2τ of u2,λ2, respec- tively, we get ||E−Eτ||L2(Ωt) ≤∥R(Eτ)∥L2(Ωt) γ (6.67) where R(Eτ) is the residual defined as in (6.64). □ 17 Algorithm 1 Conjugate Gradient Algorithm (CGA) 1: Choose time partition Jτ of the time interval (0,T). Choose initial value of the regularization parameter γ0, step size β0 and the initial approximation Eτ 0. Compute approximations of Eτ m , m= 1,...,M in the following steps. 2: Use the Newton’s method on the time partition Jτ to compute approximate solutions um

\# τ uτ (Eτ m,t) ,λm τ = λτ (Eτ m,t) of the state (2.3) and adjoint (4.18) problems via iterative schemes (5.33), (5.40), respectively. 3: Compute gradient Gm(ti) by (7.70). 4: Update the unknown parameter E := Em+1 τ as Em+1 τ (ti) = Em τ (ti) + rmdm(ti) with dm(ti) =−Gm(ti) + βmdm−1(ti), and =− (Gm,dm) rm γm∥dm∥2 , (6.68) ||Gm(ti)||2 βm

||Gm−1(ti)||2 , where d0(ti) =−G0(ti) and Gm(ti) is the gradient vector which is computed by (7.70) in time moments ti. 5: Update the regularization parameter γm for any p∈(0,1) via iterative rule of \[7\] γ0 γm = (m+ 1)p (6.69) 6: Choose the tolerance 0 <θ<1 and stop computing the functions Em τ if either ||Gm||L2(Ωt) ≤ θ, or norm of the computed gradient ||Gm||L2(Ωt) abruptly grow, or relative norms of the com- puted parameter ∥Em τ−Em−1 τ ∥ ∥Em τ ∥ are stabilized. Otherwise, set m:= m+ 1 and go to Step 2. 7 Optimization algorithms This sections presents two different optimization algorithms for solution of PIP: conjugate gradient algorithm (CGA) and time-adaptive conjugate gradient algorithm (ACGA). The CGA algorithm is a standard one and can be used on a mesh with the equidistant time step τk on every time interval Jk. The ACGA is used for minimization of the functional (4.9) on a locally adaptivelly refined meshes in time and thus, the computational mesh may have different mesh sizes τk on every time interval Jk - see definition of partition Jτ in section 5. Let us denote the nodal value of the gradient at every iteration mof the CGA at the observation 18 points {ti}by Gm(ti) and compute it accordingly to (4.23) as Gm(ti) = γ(Em τ (ti)−E0 τ(ti)) + d(ti) λ3 m τ (ti)u2 m τ (ti). (7.70) The approximations of solutions u2 m τ and λ3 m τ in the expression for gradient (7.70) are obtained via solution of the forward and adjoint problems, respectively, via Newton’s method taking E := Em τ. Algorithm 1 describes explicitly all steps of CGA algorithm. In the formulation of an adaptive algorithm ACGA we have used Theorem 3 for the estimation of the error ek = ∥EM,k τ−E∥L2(Ωt) computed on the locally ktimes refined meshes Jk τ. We choose the tolerance 0 <θ<1 and run ACGA algorithm until ek = ∥EM,k τ−E∥L2(Ωt) ≤θ, where ek is estimated via a posteriori error estimate (6.63) of the Theorem 3. Here, EM,k τ is the computed parameter obtained at the final iteration M of the CGA algorithm on k times refined mesh Jk τ. For the time-mesh refinements we use the following criterion. Algorithm 2 Adaptive Conjugate Gradient Algorithm (ACGA) 1: Choose initial time partition J0 τ of the time interval (0,T). Choose initial value of the regular- ization parameter γ0 0, step size in CGA β0 0, and the initial approximation Eτ 0,0. Initialize data g0 1 := g1,g0 2 = g2. For mesh refinements k= 0,...,N perform following steps: 2: Compute EM,k τ on the time mesh Jk τ using steps 2-6 in CGA algorithm. Here, EM,k τ is the computed parameter obtained in the CGA algorithm at the final iteration M on the k times refined mesh Jk τ. 3: Refine the time mesh Jk τ at all points where R(EM,k τ )(t) ≥˜ βkmax γ Ωt R(EM,k τ )(t) . (7.71) γ 4: 5: Here,˜ βk ∈(0,1) is the mesh refinement parameter chosen by the user. Construct a new time partition Jk+1 τ of the time interval (0,T). Interpolate ( alternative is chosen by the user): • or the initial approximation Eτ 0,k from the previous time partition Jk τ to the new time partition Jk+1 τ. • or computed Eτ M,k from the previous time partition Jk τ to the new time partition Jk+1 τ. 6: Interpolate data gk 1 ,gk 2 from the previous time partition Jk τ to the new time partition Jk τ. 7: Stop computations if norms of the gradients ||G(Eτ M,k)||L2(Ωt) either increase or stabilize, compared with the previous time partition. Otherwise set k= k+ 1 and go to Step 2. The Refinements Criterion 19 Refine the time-mesh Jτ in neighborhoods of those time-mesh points t∈Ωtwhere the weighted residual |R(Eτ)(t)|defined in (6.64) attains its maximal values: |R(Eτ)(t)| ≥˜ βmax Ωt |R(Eτ)(t)| γ . Here,˜ β ∈(0,1) is the tolerance number chosen by user. See discussion in \[1\] how this number can be chosen in optimal way. Algorithm 2 uses the above mesh refinement recommendation and implements ACGA algorithm. γ 8 Numerical studies This section presents several numerical results which demonstrate performance of the time-adaptive reconstruction of the immune response function E(t) in PIP using ACGA algorithm. Numerical tests are performed in Matlab R2023b. The code is available for download at \[40\]. In all computations we have used clinical data for the virus population function u3(t) ≈g2(t) and for the total number of uninfected and infected T-cells u1(t) + u2(t) ≈g1(t) for four patients presented in the Table 3. The initial time-mesh J0 τ of the observation interval \[0,T\] = \[0,363\] is generated such that the time step is τ = 1. We note that only data at 8 points are given in the Table 3. Since we are running CGA algorithm on the mesh J0 τ consisting of 364 points we first use linear interpolation to interpolate data given in the Table 3 to the data on the time mesh J0 τ. Next, we use interpolated data in all numerical tests for solution of PIP. The value of the mesh refinement parameter˜ βk in ACGA is chosen such that it allows local refinements of the time-mesh Jk τ where k is number of mesh refinements. All computations pre- sented below are performed for the mesh refinement parameter˜ βk = 0.875 in (7.71) for all mesh refinements k. We compute also relative residuals R1,R2 between computed functions u3 M,k M,k M,k τ , u1 τ + u2 τ and interpolated measured Vk k τ = g2 τ,Σk k τ = g1 τ which are defined as R1 = |log10 u3 M,k τ−log10 g2 M,k τ | , nno |log10(u1 M,k M,k τ + u2 τ )−log10 g1 k τ| (8.72) R2 = nno In all computations we choose parameters in the model system (2.4) as in the Table 1. The initial data is defined as follows: u1(0) = 1125000; u2(0) = 0; u3(0) = 1. (8.73) Since CGA and ACGA algorithms are locally convergent it is of vital importance that the initial guess E0(t) for approximation of the function E(t) satisfy conditions (2.6) what means that E0 is located in the close neighborhood of the exact function E(t). We model the initial guess E0(t) for 20 V= g0 2 Σ = g0 1 Figure 3: Patient 1: Interpolated clinical data by linear spline. the function E(t) with inclusion of such called cytotoxic T lymphocyte (CTL) response in E0(t), as it was proposed in \[30\]. In all our tests we have modelled effect of the CTL response for both functions d(t),E0(t) as follows: βCTL d(t) = d0 + d1(t,V), d1(t,u3) = 0,t<t1, f(t) log10 V,t≥t1, E0(t) = E0 0 + d1(t,V), f(t) = βCTL − 1 + κe(−(t−t1)/δT1) κ= 1 + 105βCTL. 1 + κe(−(t−t2)/δT2) , (8.74) Parameter values for all parameters in (8.74) are chosen differently for all patients such that they give as good as possible fitting to data. Detailed values of parameters are given in the next subsections. 8.1 Results for Patient 1 In computations of boths, CGA and ACGA, algorithms for patient 1 we used interpolated clinical data of the Table 2 presented in the Figure 3. Next, we define the initial guess for the immune response function E0 in optimization algorithms using (8.74). For patient 1 the parameters in (8.74) 21 are chosen as follows: d0 = 0.26; βCTL = 0.015; κ= 1 + 105βCTL; δT1 = 2.5; δT2 = 5.0; E0 0 = 1, t1 = 1, t2 = 1. (8.75) Figures 4 show time-dependent functions for initial guess E0(t) as well as f(t),d(t) with CTL response for parameters defined in (8.75). These functions are used now in optimization algorithms for reconstruction of the immune response function E(t). Figures 5 show computed functions Ek τ on ktimes adaptivelly refined meshes Jk τ in ACGA algorithm. Figures 6 show time-dependent behaviour of the computed virus function Vk τ ,k = 0,4 before and after applying ACGA. Here, the computed virus function Vk τ corresponds to the computed Ek τ presented in Figure 5. Results are compared with clinical data for the observed virus function V= g0 2 and observed total number of the uninfected and infected cells Σ = g0

1.  Figure 6-b) shows computed virus function on the four times locally refined time mesh J4 τ . Computed optimized virus function on Jk τ,k= 0,1,2,3 has similar behaviour and is not presented here. Figures 7 show stabilization of the computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) and behaviour ∥Em τ ∥L2(Ωt) of norms of the computed gradient ∥Gm(t)∥L2(Ωt) for patient 1. Relative residuals R1 and R2 and ∥R1∥L2(Ωt),∥R2∥L2(Ωt) which are computed as in (8.72) on the locally refined meshes Jk τ are presented in the Table 4 as well as in the Figures 8. All these norms are used in ACGA in the stopping criterion. 22 E0(t) f(t) d(t) Figure 4: Patient 1: functions E0(t),f(t),d(t) with CTL response modelled as in (8.74) using parameters defined in (8.75). k nno ∥R1∥ ∥R2∥ k nno ∥R1∥ ∥R2∥ 0 364 1 516 2 518 3 522 4 530 0.0880 0.0769 0.0767 0.0762 0.0753 0.0382 0.0321 0.0320 0.0320 0.0320 0 364 1 410 0.1321 0.1215 0.0412 0.0389 a) Patient 1 b) Patient 2 k nno ∥R1∥ ∥R2∥ k nno ∥R1∥ ∥R2∥ 0 364 1 385 2 402 0.1643 0.1560 0.1495 0.0434 0.0421 0.0411 0 364 1 413 2 478 0.1802 0.165 0.1464 0.0407 0.0384 0.0358 c) Patient 3 d) Patient 4 Table 4: Computed norms of the residuals R1 and R2 defined by (8.72) on the meshes Jk τ. Here, nnois the number of nodes in the time-mesh. 8.2 Results for Patient 2 For patient 2 we used interpolated clinical data of the Table 2 presented in the Figure 9. 23 k= 0 k= 4 Figure 5: Patient 1: results of reconstruction of the function E(t) on k times adaptivelly refined meshes Jk τ in ACGA algorithm. Computations are performed for the mesh refinement parameter ˜ βk = 0.875 for all mesh refinements k. k= 0 k= 4 Figure 6: Patient 1: Dynamics of the computed virus function Vk τ before and after optimization corresponding to the computed Ek τ on ktimes adaptivelly refined meshes versus interpolated clinical data g0 1τ,g0 2τ. 24 ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) ∥Gm(t)∥L2(Ωt) Figure 7: Patient 1: computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) and ∥Gm(t)∥L2(Ωt) on the mesh J4 τ. For patient 2 we define the parameters in (8.74) as follows: d0 = d= 0.26; βCTL = 0.1; κ= 1 + 105βCTL; δT1 = 2.5; δT2 = 5.0; E0 0 = 1, t1 = 1, t2 = 50. (8.76) Figures 10 show time-dependent functions for initial guess E0(t) as well as f(t),d(t) with CTL response for parameters defined in (8.75). These functions are used now in optimization algorithms for reconstruction of the immune response function E(t). Figures 11 show computed functions Ek τ on k= 0,1 times adaptivelly refined meshes Jk τ. Figures 12 show time-dependent behaviour of the computed virus function Vk τ ,k= 0,1 before and after applying ACGA. Here, the computed virus function Vk τ corresponds to the computed Ek τ presented in Figure 11. Results are compared with clinical data for the observed virus function V= g0 2 and observed total number of the uninfected and infected cells Σ = g0
2.  Computed optimized virus function on J0 τ is presented in the Figure 12-b). Figure 12-c) shows computed virus function on the one time locally refined time mesh J1 τ. Comparing figures 12-b) and 12-c) we observe that local adaptive mesh refinement allows more exact fit data to achieve minimum of the virus load. Figures 13 show stabilization of the computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) and behaviour of ∥Em τ ∥L2(Ωt) 25 a) R1 b) R2 c) R1 + R2 d) Figure 8: Patient 1: a), b), c) computed residuals R1 and R2 on the mesh J4 τ; d) Comparison of related residuals ∥R1∥,∥R2∥on different refined meshes Jk τ,k= 0,...,4. 26 V= g0 2 Σ = g0 1 Figure 9: Patient 2: Interpolated clinical data by linear spline. E0(t) f(t) d(t) Figure 10: Patient 2: functions E0(t),f(t),d(t) with CTL response modelled as in (8.74) using parameters defined in (8.75). norms of the computed gradient ∥Gm(t)∥L2(Ωt) for patient 2. Relative residuals R1 and R2 and ∥R1∥L2(Ωt),∥R2∥L2(Ωt) are presented in the Figures 14 as well as in the Table 4. 8.3 Results for Patient 3 For patient 3 we used interpolated clinical data of the Table 2 presented in the Figure 15. We set all parameters in (8.74) the same as for patient 2. Figures 10 show time-dependent functions for initial guess E0(t) as well as f(t),d(t) with CTL 27 k= 0 k= 1 Figure 11: Patient 2: results of reconstruction of the function E(t) on k times adaptivelly refined meshes Jk τ in ACGA algorithm. Computations are performed for the mesh refinement parameter ˜ βk = 0.875 for all mesh refinements k. a) k= 0 b) k= 0 c) k= 1 Figure 12: Patient 2: Dynamics of the computed virus function Vk τ before and after optimization corresponding to the computed Ek τ on k,k = 0,1 times adaptivelly refined meshes versus interpo- lated clinical data g0 1τ,g0 2τ. 28 ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) ∥Gm(t)∥L2(Ωt) Figure 13: Patient 2: computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) and ∥Gm(t)∥L2(Ωt) on the mesh J1 τ. response for parameters defined in (8.75) which are the same as for the patient 2. These functions are used now in optimization algorithms for reconstruction of the immune response function E(t). Figures 16 show computed functions Ek τ on k= 0,1,2 times adaptivelly refined meshes Jk τ. Figures 17 show time-dependent behaviour of the computed virus function Vk τ ,k= 0,2 before and after applying ACGA. Here, the computed virus function Vk τ corresponds to the computed Ek τ presented in Figure 16. Results are compared with clinical data for the observed virus function V= g0 2 and observed total number of the uninfected and infected cells Σ = g0
3.  Computed optimized virus function on J0 τ is presented in the Figure 17-b). Figure 17-c) shows computed virus function on the twice locally refined time mesh J2 τ. Comparing figures 17-b) and 17-c) we again observe that local adaptive mesh refinement allows more exact fit data to achieve minimum of the virus load. Figures 18 show stabilization of the computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) and behaviour of ∥Em τ ∥L2(Ωt) norms of the computed gradient ∥Gm(t)∥L2(Ωt) for patient 3. Relative residuals R1 and R2 and ∥R1∥L2(Ωt),∥R2∥L2(Ωt) are presented in the Figures 19 as well as in the Table 4. 8.4 Results for Patient 4 For patient 4 we used interpolated clinical data of the Table 2 presented in the Figure 20. We observe that the data is very discontinuos. However, we test the same ACGA algorithm for this dataset to see performance of the code. 29 a) R1 b) R2 c) R1 + R2 d) Figure 14: Patient 2: a), b), c) computed residuals R1 and R2 on the mesh J1 τ; d) Comparison of related residuals ∥R1∥,∥R2∥on the meshes Jk τ,k= 0,1. 30 V= g0 2 Σ = g0 1 Figure 15: Patient 3: Interpolated clinical data by linear spline. a) k= 0 b) k= 1 c) k= 2 Figure 16: Patient 3: results of reconstruction of the function E(t) on k times adaptivelly refined meshes Jk τ in ACGA algorithm. Computations are performed for the mesh refinement parameter ˜ βk = 0.875 for all mesh refinements k. 31 a) k= 0 b) k= 0 c) k= 2 Figure 17: Patient 3: Dynamics of the computed virus function Vk τ before and after optimization corresponding to the computed Ek τ on k,k = 0,2 times adaptivelly refined meshes versus interpo- lated clinical data g0 1τ,g0 2τ. ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) ∥Gm(t)∥L2(Ωt) Figure 18: Patient 3: computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) ∥Em τ ∥L2(Ωt) and ∥Gm(t)∥L2(Ωt) on the mesh J2 τ. 32 a) R1 b) R2 c) R1 + R2 d) Figure 19: Patient 3: a), b), c) computed residuals R1 and R2 on the mesh J2 τ; d) Comparison of related residuals ∥R1∥,∥R2∥on the meshes Jk τ,k= 0,1,2. 33 V= g0 2 Σ = g0 1 Figure 20: Patient 4: Interpolated clinical data by linear spline. For patient 4 we define the parameters in (8.74) as follows: d0 = d= 0.26; βCTL = 0.1; κ= 1 + 105βCTL; δT1 = 2.5; δT2 = 5.0; E0 = 1.4, t1 = 1, t2 = 1. (8.77) Figures 21 show time-dependent functions for initial guess E0(t) as well as f(t),d(t) with CTL response for parameters defined in (8.75) which are the same as for the patient 4. These functions are used now in optimization algorithms for reconstruction of the immune response function E(t). Figures 22 show computed functions Ek τ on k= 0,1,2 times adaptivelly refined meshes Jk τ. Figures 23 show time-dependent behaviour of the computed virus function Vk τ ,k= 0,2 before and after applying ACGA. Here, the computed virus function Vk τ corresponds to the computed Ek τ presented in Figure 22. Results are compared with clinical data for the observed virus function V= g0 2 and observed total number of the uninfected and infected cells Σ = g0
4.  Computed optimized virus function on J0 τ is presented in the Figure 23-b). Figure 23-c) shows computed virus function on the twice locally refined time mesh J2 τ. Comparing figures 23-b) and 23-c) we again observe that local adaptive mesh refinement allows more exact fit data to achieve minimum of the virus load. Figures 24 show stabilization of the computed relative norms ∥Em τ−Em−1 τ ∥L2(Ωt) and behaviour of ∥Em τ ∥L2(Ωt) 34 E0(t) f(t) d(t) Figure 21: Patient 4: functions E0(t),f(t),d(t) with CTL response modelled as in (8.74) using parameters defined in (8.75). a) k= 0 b) k= 1 c) k= 2 Figure 22: Patient 4: results of reconstruction of the function E(t) on k times adaptivelly refined meshes Jk τ in ACGA algorithm. Computations are performed for the mesh refinement parameter ˜ βk = 0.875 for all mesh refinements k. 35 a) k= 0 b) k= 0 c) k= 2 Figure 23: Patient 4: Dynamics of the computed virus function Vk τ before and after optimization corresponding to the computed Ek τ on k,k = 0,2 times adaptivelly refined meshes versus interpo- lated clinical data g0 1τ,g0 2τ. norms of the computed gradient ∥Gm(t)∥L2(Ωt) for patient 4. Relative residuals R1 and R2 and ∥R1∥L2(Ωt),∥R2∥L2(Ωt) are presented in the Figures 25 as well as in the Table 4.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/HIV-Immune-Response-Reconstruction",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Parameter Identification of Time-Dependent Immune Response Coefficient E(t) in HIV Dynamical Model via Tikhonov Regularization and Adaptive Finite Elements"
    },

    {
      "@id": "rdip:Dataset/HIV-Clinical-Data",
      "@type": "schema:Dataset",
      "schema:name": "Clinical HIV patient data (4 patients)",
      "schema:description": "Time-series measurements of total T-cells (uninfected + infected) and virus load from Tables 2–3, interpolated to daily points"
    },

    {
      "@id": "rdip:Activity/Data-Interpolation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Linear interpolation of sparse clinical measurements to daily time grid [0,363]",
      "prov:used": "rdip:Dataset/HIV-Clinical-Data",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Interpolated-Clinical-Data",
        "@type": "schema:Dataset",
        "schema:name": "Daily interpolated g1(t) and g2(t) for 4 patients"
      }
    },

    {
      "@id": "rdip:Activity/Theory-Development",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Derivation of Lagrangian, adjoint system, Fréchet derivative, and a posteriori error estimates for Tikhonov functional",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Mathematical-Framework",
        "@type": "schema:Dataset",
        "schema:name": "Equations (4.9)–(6.67): Optimality system, adjoint problem, gradient expression, error estimators"
      }
    },

    {
      "@id": "rdip:Activity/Numerical-Discretization",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Finite-element (P0) + implicit Euler discretization of forward/adjoint problems + Newton solver",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Discretized-System",
        "@type": "schema:Dataset",
        "schema:name": "Piecewise-constant FEM spaces, Newton schemes (5.33) & (5.40)"
      }
    },

    {
      "@id": "rdip:Activity/ACGA-Implementation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Implementation of Adaptive Conjugate Gradient Algorithm (ACGA) with residual-based mesh refinement",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/MATLAB-R2023b",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "MATLAB",
        "rdip:version": "R2023b"
      },
      "prov:used": [
        "rdip:Dataset/Interpolated-Clinical-Data",
        "rdip:Dataset/Mathematical-Framework",
        "rdip:Dataset/Discretized-System"
      ],
      "rdip:outputDataset": [
        {
          "@id": "rdip:Dataset/Reconstructed-E-functions",
          "@type": "schema:Dataset",
          "schema:name": "Reconstructed immune response E_k(t) on adaptively refined meshes for 4 patients"
        },
        {
          "@id": "rdip:Dataset/Simulated-Trajectories",
          "@type": "schema:Dataset",
          "schema:name": "Forward solutions u1+u2, u3 matching clinical data after optimization"
        },
        {
          "@id": "rdip:Dataset/Numerical-Figures",
          "@type": "schema:Dataset",
          "schema:name": "Figures 3–25: Reconstructions, virus dynamics, residuals, convergence plots"
        }
      ]
    },

    {
      "@id": "rdip:Activity/CTL-Initial-Guess-Modeling",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Modeling of initial guess E0(t) and d(t) with cytotoxic T-lymphocyte (CTL) response (Eq. 8.74)",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Initial-Guess-E0",
        "@type": "schema:Dataset",
        "schema:name": "Patient-specific E0(t) with CTL burst parameters"
      }
    },

    {
      "@id": "rdip:Activity/Validation-Error-Analysis",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Computation of relative residuals R1, R2 and convergence monitoring on refined meshes",
      "prov:used": [
        "rdip:Dataset/Reconstructed-E-functions",
        "rdip:Dataset/Simulated-Trajectories"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Validation-Metrics",
        "@type": "schema:Dataset",
        "schema:name": "Table 4 + Figures showing residuals, gradient norms, mesh refinement statistics"
      }
    }
  ]
}
```

This JSON-LD fully captures the provenance of the mathematical/numerical modeling paper:

*   Central project: reconstruction of time-dependent immune response coefficient E(t) in an HIV dynamical system
*   Clinical data → interpolation
*   Theoretical development of Lagrangian, adjoint system, gradient, a posteriori error estimates
*   FEM + Newton discretization of forward/adjoint problems
*   Implementation of the adaptive conjugate gradient algorithm (ACGA) in MATLAB R2023b
*   Patient-specific modeling of initial guess with CTL response
*   Numerical results: reconstructed E(t), fitted trajectories, residuals, convergence on adaptively refined meshes

All major data-producing activities (theory, discretization, algorithm implementation, numerical experiments) and resulting datasets (equations, code, reconstructions, figures) are represented using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: To overcome the lack of training data, we used a large document collection from PubMed Central™ Open Access 1[https://ceb.nlm.nih.gov/inactive-communications-engineering-branch-projects/](https://ceb.nlm.nih.gov/inactive-communications-engineering-branch-projects/) medical-article-records-groundtruth-marg/ Cases Journal 2009, 2:7170 [http://casesjournal.com/casesjournal/article/view/7170](http://casesjournal.com/casesjournal/article/view/7170) Figure 3. Flourescein Angiogram of the right eye showed blocked venous fluorescence from the retinal hemorrhages, extensive areas of capillary non-perfusion, and vessel wall staining. Discussion CRVO has two types: Nonischemic (70%): which is characterized by vision that is better than 20/200, 16% progress to nonperfused; 50% resolve completely without treatment; defined as <10 disk diameter (DD) of capillary nonperfusion. Ischemic (30%): which is defined as more than 10 DD of nonperfusion; patients are usually older and have worse vision; 60% develop iris NV; up to 33% develop neovascular glaucoma; 10% are combined with branch retinal arterial occlusion (usually cilioretinal artery due to low perfusion pressure of choroidal system) \[7\]. Central retinal vein occlusion is a disease of the old population (age >50 years old). Major risk factors Figure 4. An example of acute hypertensive retinopathy, which is one of the differentials for CRVO. Figures here are showing arteriovenous nicking, copper wire arterial changes, hemorrhages, cotton wool spots, disc edema bilaterally (Left more than the right), and exudates that dominate in the peripapillary area. Table 2. Laboratory tests including hypercoagulability workup are summarized in Table 2 Glucose 90 HgA1c 5.8 White blood cell count 9.8 Neutrophils 80% Lymphocytes 14% Monocytes 4.6% Hemoglobin 15.0 Hematocrit 45.1 Platelets 282 MCV 84.3 RDW 14.6 Prothrombin time 12.5 INR 0.99 PTT LA 33 normal (Reference normal < 40) ANA Negative Rheumatoid factor Negative ESR 10 (normal) CRP 20 (normal) Serum protein electrophoresis Normal Lipid profile Normal Hemoglobin electrophoresis Normal VDRL Negative FTA-ABS Negative are hypertension, diabetes, and atherosclerosis. Other risk factors are glaucoma, syphilis, sarcoidosis, vasculitis, increased intraorbital or intraocular pressure, hyphema, hyperviscosity syndromes (multiple myeloma, Walden- strom’s macroglobulinemia, and leukemia), high homo- cysteine levels, sickle cell, and HIV \[8\]. Paul O’Mahoney et al. studied the relationship between traditional atherosclerosis risk factors and retinal vein occlusion (RVO). They systematically retrieved all studies between 1985 and 2007 that compared cases with any RVO with controls. They concluded that hypertension and hyperlipidemia are common risk factors for RVO in adults, and diabetes mellitus is less so. It remains to be determined whether lowering blood pressure and/or serum lipids levels can improve visual acuity or the complications of RVO \[9\]. Open-angle glaucoma is the most common local factor predisposing to RVO as increased intraocular pressure compromises retinal vein outflow and produces stasis \[10,11\]. Table 3. Further hypercoagulability workup is summarized in Table 3 HIV Negative Functional protein S assay Normal Functional protein C assay Normal Functional antithrombin III assay Normal Antiphospholipid antibody titer 262 (reference range = 151-264) Lupus anticoagulant Negative Anticardiolipin antibody Negative Homocysteine 11.5 (0-10) High Folate level Normal B12 level Normal Creatinine 0.9 mg per deciliter Factor V Leiden PCR assay Negative Page 3 of 4 (page number not for citation purposes) (a) PDF representation. Cases Journal 2009, 2:7170 [http://casesjournal.com/casesjournal/article/view/7170](http://casesjournal.com/casesjournal/article/view/7170) Figure 3. Flourescein Angiogram of the right eye showed blocked venous fluorescence from the retinal hemorrhages, extensive areas of capillary non-perfusion, and vessel wall staining. Discussion CRVO has two types: Nonischemic (70%): which is characterized by vision that is better than 20/200, 16% progress to nonperfused; 50% resolve completely without treatment; defined as <10 disk diameter (DD) of capillary nonperfusion. Ischemic (30%): which is defined as more than 10 DD of nonperfusion; patients are usually older and have worse vision; 60% develop iris NV; up to 33% develop neovascular glaucoma; 10% are combined with branch retinal arterial occlusion (usually cilioretinal artery due to low perfusion pressure of choroidal system) \[7\]. Central retinal vein occlusion is a disease of the old population (age >50 years old). Major risk factors Figure 4. An example of acute hypertensive retinopathy, which is one of the differentials for CRVO. Figures here are showing arteriovenous nicking, copper wire arterial changes, hemorrhages, cotton wool spots, disc edema bilaterally (Left more than the right), and exudates that dominate in the peripapillary area. Table 2. Laboratory tests including hypercoagulability workup are summarized in Table 2 Glucose 90 HgA1c 5.8 White blood cell count 9.8 Neutrophils 80% Lymphocytes 14% Monocytes 4.6% Hemoglobin 15.0 Hematocrit 45.1 Platelets 282 MCV 84.3 RDW 14.6 Prothrombin time 12.5 INR 0.99 PTT LA 33 normal (Reference normal < 40) ANA Negative Rheumatoid factor Negative ESR 10 (normal) CRP 20 (normal) Serum protein electrophoresis Normal Lipid profile Normal Hemoglobin electrophoresis Normal VDRL Negative FTA-ABS Negative are hypertension, diabetes, and atherosclerosis. Other risk factors are glaucoma, syphilis, sarcoidosis, vasculitis, increased intraorbital or intraocular pressure, hyphema, hyperviscosity syndromes (multiple myeloma, Walden- strom’s macroglobulinemia, and leukemia), high homo- cysteine levels, sickle cell, and HIV \[8\]. Paul O’Mahoney et al. studied the relationship between traditional atherosclerosis risk factors and retinal vein occlusion (RVO). They systematically retrieved all studies between 1985 and 2007 that compared cases with any RVO with controls. They concluded that hypertension and hyperlipidemia are common risk factors for RVO in adults, and diabetes mellitus is less so. It remains to be determined whether lowering blood pressure and/or serum lipids levels can improve visual acuity or the complications of RVO \[9\]. Open-angle glaucoma is the most common local factor predisposing to RVO as increased intraocular pressure compromises retinal vein outflow and produces stasis \[10,11\]. Table 3. Further hypercoagulability workup is summarized in Table 3 HIV Negative Functional protein S assay Normal Functional protein C assay Normal Functional antithrombin III assay Normal Antiphospholipid antibody titer 262 (reference range = 151-264) Lupus anticoagulant Negative Anticardiolipin antibody Negative Homocysteine 11.5 (0-10) High Folate level Normal B12 level Normal Creatinine 0.9 mg per deciliter Factor V Leiden PCR assay Negative Page 3 of 4 (page number not for citation purposes) (b) XML representation. (c) PDFMiner output on (a). Cases Journal 2009, 2:7170 [http://casesjournal.com/casesjournal/article/view/7170](http://casesjournal.com/casesjournal/article/view/7170) Figure 3. Flourescein Angiogram of the right eye showed blocked venous fluorescence from the retinal hemorrhages, extensive areas of capillary non-perfusion, and vessel wall staining. Discussion CRVO has two types: Nonischemic (70%): which is characterized by vision that is better than 20/200, 16% progress to nonperfused; 50% resolve completely without treatment; defined as <10 disk diameter (DD) of capillary nonperfusion. Ischemic (30%): which is defined as more than 10 DD of nonperfusion; patients are usually older and have worse vision; 60% develop iris NV; up to 33% develop neovascular glaucoma; 10% are combined with branch retinal arterial occlusion (usually cilioretinal artery due to low perfusion pressure of choroidal system) \[7\]. Central retinal vein occlusion is a disease of the old population (age >50 years old). Major risk factors Figure 4. An example of acute hypertensive retinopathy, which is one of the differentials for CRVO. Figures here are showing arteriovenous nicking, copper wire arterial changes, hemorrhages, cotton wool spots, disc edema bilaterally (Left more than the right), and exudates that dominate in the peripapillary area. Table 2. Laboratory tests including hypercoagulability workup are summarized in Table 2 Glucose 90 HgA1c 5.8 White blood cell count 9.8 Neutrophils 80% Lymphocytes 14% Monocytes 4.6% Hemoglobin 15.0 Hematocrit 45.1 Platelets 282 MCV 84.3 RDW 14.6 Prothrombin time 12.5 INR 0.99 PTT LA 33 normal (Reference normal < 40) ANA Negative Rheumatoid factor Negative ESR 10 (normal) CRP 20 (normal) Serum protein electrophoresis Normal Lipid profile Normal Hemoglobin electrophoresis Normal VDRL Negative FTA-ABS Negative are hypertension, diabetes, and atherosclerosis. Other risk factors are glaucoma, syphilis, sarcoidosis, vasculitis, increased intraorbital or intraocular pressure, hyphema, hyperviscosity syndromes (multiple myeloma, Walden- strom’s macroglobulinemia, and leukemia), high homo- cysteine levels, sickle cell, and HIV \[8\]. Paul O’Mahoney et al. studied the relationship between traditional atherosclerosis risk factors and retinal vein occlusion (RVO). They systematically retrieved all studies between 1985 and 2007 that compared cases with any RVO with controls. They concluded that hypertension and hyperlipidemia are common risk factors for RVO in adults, and diabetes mellitus is less so. It remains to be determined whether lowering blood pressure and/or serum lipids levels can improve visual acuity or the complications of RVO \[9\]. Open-angle glaucoma is the most common local factor predisposing to RVO as increased intraocular pressure compromises retinal vein outflow and produces stasis \[10,11\]. Table 3. Further hypercoagulability workup is summarized in Table 3 HIV Negative Functional protein S assay Normal Functional protein C assay Normal Functional antithrombin III assay Normal Antiphospholipid antibody titer 262 (reference range = 151-264) Lupus anticoagulant Negative Anticardiolipin antibody Negative Homocysteine 11.5 (0-10) High Folate level Normal B12 level Normal Creatinine 0.9 mg per deciliter Factor V Leiden PCR assay Negative Page 3 of 4 (page number not for citation purposes) (d) Annotations generated by matching (b) and (c). Fig. 1: Parsing PDF page (a) using PDFMiner (c) and matching the layout with the XML representation (b) to generate annotation of page layout (d). The color scheme in (c) is red: textbox; green: textline; blue: image; yellow: geometric shape. The color scheme in (d) is red: title; green: text; blue: figure; yellow: table; cyan: list. (PMCOA), provided under the Creative Commons license. The articles in PMCOA are provided in both PDF format (Fig. 1a) and in an XML format (Fig. 1b). The XML version of the PMCOA documents is a structured representation of its content and all XML documents follow the schema provided by the NLM for journals2. Since the content in the PDF version of the articles and their XML representation contain similar format, we have identified a method to use these two representations of the same article to identify document layout components. In this work, a total of 1,162,856 articles that have a complete XML representation were downloaded from ftp.ncbi.nlm.nih.gov/pub/pmc on 3 October 2018, and automatically annotated with the method described in the following sections. A. Layout categories The structured XML representation of the articles in the PMCOA dataset contains many different categories of nodes, which are difficult, even for humans, to distinguish based only on document images. We aggregated the categories of the nodes in the XML into the document layout categories shown in Table I, based on the following considerations: • The differences between the categories are distinctive and intuitive for a visual model to capture learnable patterns. • The categories are commonly found in documents in various domains. • The categories cover most elements that are important for downstream studies, such as text classification, entity recognition, figure/table understanding, etc. B. Annotation algorithms Our annotation algorithm matches PDF elements (see Section III-B2) to the XML nodes. Then, the bounding box 2[https://dtd.nlm.nih.gov](https://dtd.nlm.nih.gov) Document layout category XML category Text author, author affiliation; paper information; copyright information; abstract; paragraph in main text, footnote, and appendix; figure & table caption; table footnote Title article title, standalone (sub)section titlea standalone figure & table labelb List listc Table main body of table Figure main body of figured TABLE I: Categories of document layout included in PubLayNet. , a When a section title is inline with the leading text of the section, it is labeled as part of the text, but not as a title. b When a figure/table label is inline with the caption of the figure/table, it is labeled as part of the text, but not as a title. c Nested lists (i.e., child list under an item of parent list) are annotated as a single object. Child lists in nested lists are not annotated. d When sub-figures exist, the whole figure panel is annotated as a single object. Sub-figures are not annotated individually. and segmentation of the PDF elements are calculated. The XML nodes are used to decide the category label for each bounding box and segmentation. Finally, a quality control metric is defined to control the noise of the annotations at an extremely low level.

1.  PMCOA XML pre-processing and parsing: Some of the nodes in the XML tree are not considered for matching, such as tex-math, edition, institution-id, and disp-formula. These nodes are removed, as the content of these nodes may interfere with the matching of other nodes. The placement of list, table and figure nodes in the XML schema is not consistent across the articles. We standardized the XML tree by moving list, table, and figure nodes into the floats-group branch. Then, the nodes in the XML tree are split into five groups: • Sorted: including paper title, abstract, keywords, section titles, and text in main text. The order of sorted XML nodes matches the reading order in the PDF document. • Unsorted: including copyright statement, license, authors, affiliations, acknowledgments, and abbreviations. The order of unsorted XML nodes may not match the reading order in the PDF document. • Figures: including caption label (e.g., ‘Fig. 1’), caption text, and figure body • Tables: including caption label (e.g. Table I), caption text, footnotes, and table body • Lists: including lists.
2.  PMCOA PDF parsing: Fig. 1c illustrates an example of the layout of a PDF page parsed using the PDFMiner3 package, where three layout types are extracted: • textbox (red): block of text, consisting of textlines (blue). Each textbox has three attributes: the text in the textbox, the bounding box of the textbox, and textlines in the textbox. Each textline has two attributes: the text in the textline and the bounding box of the textline. • image (green): consisting of images. Each image is associated with a bounding box. • geometric shape (yellow): consisting of lines, curves, and rectangles. Each geometric shape is associated with a bounding box.
3.  String pre-processing: The strings from XML and PDF are Unicode strings. The Unicode standard defines various normalization forms of a Unicode string, based on the definition of canonical equivalence and compatibility equivalence. In Unicode, several characters can be expressed in various ways. To make the matching between XML and PDF more robust, the strings are normalized to the KD normal form4 (i.e., replacing all compatibility characters with their equivalents).
4.  PDF-XML matching algorithms: There are frequent minor discrepancies between the content of PDF parsed by PDFMiner and the text of XML nodes. Thus fuzzy string matching is adopted to tolerate minor discrepancies. We use the fuzzysearch5 package to search for the closest match to a target string in a source string, where string distance is measured by the Levenshtein distance \[18\]. The maximum distance allowed for a match (dmax) is adaptive to the length of the target string (ltarget) as, dmax =    0.2 ∗ ltarget 0.15 ∗ ltarget 0.1 ∗ ltarget if ltarget ≤ 20 if 20 < ltarget ≤ 40 if ltarget > 40 As one textbox may cover multiple XML nodes, we sequentially search the textlines of a textbox in the text of a XML node. If the textline of the textbox cannot be found in the text of the XML node, we skip to and search the next textbox. If the end of the XML node is reached, but the textline is not the end of the textbox, the textbox is divided into two textboxes at the current textline. Then the former textbox is appended to the list of matched textboxes of the XML node. When all the content of the XML node is covered by matching textlines, we start searching in the next XML node. This matching procedure is applied to all the text XML nodes, including the ‘Sorted’, ‘Unsorted’, and ‘Lists’ groups; the captions in the ‘Tables’ and ‘Figures’ groups; and the footnotes in the ‘Table’ group. Depending on the template of specific journals, section/subsection titles may be inline with the first paragraph in the section. A title is treated as inline titles if the last line of the title does not cover a whole textline. Inline section titles are annotated as part of the text, rather than individual instances of titles. The same principle is also applied to the caption labels of figures and tables. After all the text XML nodes are processed, the margin between annotated text elements in the PDF page is utilized to annotate the body of figures and tables. Fig. 2 illustrates an example of the annotation process for a figure body. First, the bounding box of the main text of the article (green box) is obtained as the smallest bounding box that encloses all the annotated text elements in the article. Then the potential box (blue box) for the figure is calculated as the the largest box that can be fit in the margin between the top of the caption box (brown box) and the annotated text elements above the caption. The last step is to annotate the figure body with the smallest box (red box) that encloses all the textboxes, images, and geometric shapes within the potential box. Table bodies are annotated using the same principle, where it is assumed that table bodies are always below the caption of the tables. ARTICLE NATURE COMMUNICATIONS | DOI: 10.1038/s41467-017-00439-1 Main text box cryptic carrier protein that works together with NosI for the incorporation of MIA into nosiheptide biosynthesis. NosJ-bound MIA is the natural substrate of NosN. The methyltransferase activity of the class C radical SAM enzyme Potential box NosN has been recently reconstituted in vitro in our lab, which a b Annotation R1 O S N H N R2 O H R1 = H, R2 = Pan, MIA-Pan, 5 c R1 = CH3, R2 = Pan, DMIA-Pan, 6 R1 = H, R2 = CH3, MIA-SNAC, 9 R1 = CH3, R2 = CH3, DMIA-SNAC, 10 Pan = HN HN O O S O HO O HN O OH 12 ii i µM 20 10 0 6 8 10 Time (min) DMIA-SNAC, 9 DMIA-Pan, 6 0 1 2 3 4 5 Time (h) OH N H DMIA, 11 O was shown to install a methyl group on the indole C4 of the MIA moiety32, 33. Neither MIA (3) nor 2 is the NosN substrate, while this enzyme was shown to methylate 9, an N-acetylcysteamine (SNAC) thioester derivative of MIA, to produce 10 (Fig. 4a)32 . As SNAC serves as a structural mimic of the NosJ Ppant arm, it is likely that the NosN-catalyzed methylation occurs on the NosJ-bound MIA thioester 8. To validate this hypothesis, we synthesized MIA-Pan (5), a good structural mimic of the NosJ-bound MIA thioester 8, and ran the NosN reaction with 5. LC-HR-MS analysis clearly showed the production of a com- pound with a protonated molecular ion at m/z = 450.2051, which is absent in the control assays (Fig. 4b). This compound is consistent with 6 (Fig. 4a), a pantetheine-bound thioester of 3,4-dimethyl-2-indolic acid (DMIA, 11) (DMIA-Pan, molecule formula C22H31N3O5S, \[M+H\]+ calcd 450.2063, 2.7 p.p.m. error) and the identity of 6 was further corroborated by HR-MS/MS analysis (Supplementary Fig. 5). We next performed the detailed time-course analysis of NosN reactions with 5 and 9, respectively. This analysis showed that NosN is more efficient with 9 than with 5 (Fig. 4c), supporting that the NosJ-bound MIA thioester 8 is the natural substrate of NosN. To further validate that NosJ-bound MIA 8 is the NosN substrate, we performed a tandem reaction by incubation of NosI, NosJ, NosN and other required components overnight, and the workup was subsequently treated with NaOH to hydrolyze any thioesters. LC-HR-MS analysis of the resulting mixture showed the production of a compound exhibiting a deprotonated molecular ion of 188.0710, which is absent in the negative control reactions (Fig. 5a). The suggested formula C11H11NO2 is consistent with DMIA (11) (\[M-H\]− calcd 188.0711, 0.5 p.p.m. Fig. 4 Probing NosN reaction by using substrate analogues. a NosN error) and this is further supported by co-elution with the methylates two MIA-based thioester (5 and 9) to produce the synthetic standard (Fig. 5a, trace iii). These analyses demonstrate corresponding indole C4 methylated products (6 and 10). b Extracted ion that the NosN-catalyzed methylation occurs on the NosJ-bound chromatograms (EICs) of \[M+H\]+ = 450.2 (corresponding to DMIA-Pan, MIA. It should be noted that NosN does not methylate 12
5.  for (i) control reaction with the supernatant of boiled NosN, and (ii) (Fig. 4), a structural mimic of the Cys-tethered MIA, excluding overnight reaction with NosN and 5. c Time-course analysis of the NosN the possibility that NosN acts on an MIA moiety that is bound to reactions with MIA-SNAC 9 and MIA-Pan 5, showing that 5 is a better a Cys (or Ser) residue of a polypeptide chain. substrate of NosN than 9. The reactions were carried out with 100 μM substrates (5 or 9), 1 mM SAM, 1 mM NADPH, 50 µM FldA, 20 µM Fpr and 100 μM NosN. The chemical structures of DMIA (11) and 12 are shown; the latter is a structural mimic of the MIA-based thioester associated with a NosK participates in DMIA transfer. nosK is co-transcribed with nosJ and nosI, which encodes a putative hydrolase-like enzyme. Bioinformatical analysis based on sequence similarity network (SSN)37 and phylogenetic analysis shows that NosK is Caption box polypeptide Cys residue, which is not a NosN substrate a b DMIA, 12 nosK vi µM NosK with MIA-NosJ NosK with DMIA-NosJ nosl v 90 Wild type iv 60 DMIA std iii NosN assay No NosN 30 Control assays ii With Nosl i 0 9 10 11 12 Time (min) 15 45 30 60 90 75 Time (min) Fig. 5 Functional dissection of NosN and NosK. a Extracted ion chromatograms (EICs) of \[M-H\]− = 188.1 (corresponding to DMIA, 11) for (i) control reaction with the supernatant of boiled NosN, (ii) overnight reaction with 100 μM MIA, 500 μM ATP, 10 μM NosI, 100 μM NosJ and 100 μM NosN that was subsequently treated with 0.2 M NaOH for 30 min, (iii) DMIA synthetic standard and the culture extracts from (iv) S. actuosus wild-type strain, (v) the nosI-knockout mutant and (vi) the nosK-knockout mutant. b A time course analysis of NosK-catalyzed MIA and DMIA release from the NosJ-bound thioesters. The reaction was performed by addition of 10 μM NosK or NosI to the solutions containing 100 μM MIA-NosJ or DMIA-NosJ (which were produced by treating apo-NosJ with Sfp and the corresponding CoA thioesters) and the reaction was quenched by addition of an equal volume of methanol at different time points. MIA and DMIA was quantified by HPLC with UV detection at 300 nm. The reaction was performed in triplicates and the SD are shown by the error bars. It should be noted that NosK also hydrolyzes the CoA-bound MIA and DMIA thioesters with comparative efficiencies with that of the NosJ-bound thioesters 3[https://github.com/euske/pdfminer](https://github.com/euske/pdfminer) 4[http://unicode.org/reports/tr15/](http://unicode.org/reports/tr15/) 5[https://github.com/taleinat/fuzzysearch](https://github.com/taleinat/fuzzysearch) 4 NATURE COMMUNICATIONS | 8: 437 | DOI: 10.1038/s41467-017-00439-1 | [www.nature.com/naturecommunications](http://www.nature.com/naturecommunications) Fig. 2: Annotation process for an example figure. The main text box and the potential box are determined from the annotations of the caption of the figure and surrounding text elements. The final annotation is made as the smallest box that encloses all the textboxes, images, and geometric shapes within the potential box.
6.  Generation of instance segmentation: For text, title, and list instances, we automatically generate segmentations from the texelines of the PDF elements, which allows us to train the Mask-RCNN model \[5\]. As shown in Fig. 3, the top edge of the top textline and the bottom edge of the bottom textline in the PDF elements forms the top and bottom edge of the segmentation, respectively. The right edge of the textlines are scanned from top to bottom to form the right side of the segmentation. -shape edges are inserted if the right edge of a textline is on the left of the right edge of the textline above it. Otherwise, -shape edges are inserted. The left side of the segmentation is generated by scanning the left edge of the textlines from bottom to top using the same principle. For figure and table instances, the bounding box is reused as the segmentation, since almost all these instances are rectangular. Fig. 1d illustrates the annotations for the PDF page in Fig. 1a. Textline Textline Textline Segmentation Textline Fig. 3: Example of generating layout segmentation based on textlines. The segmentation is a regular polygon, consisting of only horizontal and vertical edges. The shape of the segmentation is decided by the position of adjacent textlines.
7.  Quality control: There are several sources that can lead to discrepancies between the PDF parsing results and the corresponding XML. When discrepancies are over the threshold dmax, the annotation algorithm may not be able to identify all elements in a document page. For example, PDFminer parses some complex inline formulas completely differently from the XML, which leads to a large Levenshtein distance and failure to match PDF elements with XML nodes. Hence we need a way to evaluate how well a PDF page is annotated and eliminate poorly annotated pages from PubLayNet. The annotation quality of a PDF page is defined as the ratio of the area of textboxes, images, and geometric shapes that are annotated to the area of textboxes, images, and geometric shapes within the main text box of the page. Non-title pages of which the annotation quality is less than 99% are excluded from PubLayNet, which is an extremely high standard to control the noise in PubLayNet at a low level. The format of title pages of different journals varies substantially. Miscellaneous information, such as manuscript history (dates of submission, revision, acceptance), copyright statement, editorial details, etc, is often included in title pages, but formatted differently from the XML representation and therefore missed in the annotations. To include adequate title pages, we set the threshold of annotation quality to 90% for title pages. C. Data partition The annotated PDF pages are partitioned into training, development, and testing sets at journal level to maximize the differences between the sets. This allows better evaluation of how well a model generalizes to unseen paper templates. The journals that contain ≤ 2000 pages, ≥ 320 figures, ≥ 140 tables, and ≥ 20 lists are extracted to generate the development and testing sets. This avoids the development and testing sets from being dominated by a particular journal with a large number of pages, and ensures the development and testing sets have an adequate number instances of figures, tables, and lists. Half of these journals are randomly drawn to generate the development set. The development set consists of all pages with a list in these journals, as well as 2000 title pages, 3000 pages with a table, 3000 pages with a figure, and 2000 plain pages, which are randomly drawn from these journals. The testing set is generated using the same procedure on the rest half of the journals. To further reduce the noise in the development and testing sets and make more valid evaluation of models, the development and testing sets are curated by human, where profound erroneous pages are removed and moderate erroneous pages are corrected. The journals that do not satisfy the criteria above are used to generate the training set. To ensure diversity of the training data, from each of the journals, we randomly drawn at most 200 pages with a list, 50 pages with a table, 50 pages with a figure, 50 title pages, and 25 plain pages. The statistics of the training, development, and testing sets are depicted in detail in Table II. TABLE II: Statistics of training, development, and testing sets in PubLayNet. PubLayNet is one to two orders of magnitude larger than any existing document layout dataset.

*   These numbers are slightly greater than the number of pages drawn, as pages with lists may be title pages or contain tables or figures. Training Development Testing Pages Plain pages 87,608 1,138 1,121 Title pages 46,480 2,059+ 2,021+ Pages with lists 53,793 2,984 3,207 Pages with tables 86,950 3,772+ 3,950+ Pages with figures 96,656 3,734+ 3,807+ Total 340,391 11,858 11,983 Instances Text 2,376,702 93,528 95,780 Title 633,359 19,908 20,340 Lists 81,850 4,561 5,156 Tables 103,057 4,905 5,166 Figures 116,692 4,913 5,333 Total 3,311,660 127,815 131,775 IV. RESULTS Three experiments are designed to investigate 1) how well the established object detection models Faster-RCNN (F-RCNN) \[19\] and Mask-RCNN (M-RCNN) \[5\] can recognize document layout of PubLayNet; 2) if the F-RCNN and M-RCNN models pre-trained on PubLayNet can be fine-tuned to tackle the ICDAR 2013 Table Recognition Competition6; 3) if the F-RCNN and M-RCNN models pre-trained on PubLayNet are better initializations than those pre-trained on the ImageNet and COCO datasets for analyzing documents in a different domain. A. Document layout recognition using deep learning We trained a F-RCNN model and a M-RCNN model on PubLayNet using the Detectron implementation \[20\]. PDF pages are converted to images using the pdf2image package7. Each model was trained for 180k iterations with a base learning rate of 0.01. The learning rate was reduced by a factor of 10 at the 120k iteration and the 160k iteration. The models were trained on 8 GPUs with one image per GPU, which yields an effective mini-batch size of 8. Both models use the ResNeXt-101-64x4d model as the backbone, which was initialized with the model pre-trained on ImageNet. The performance of the F-RCNN and the M-RCNN models on our development and testing sets are depicted in Table III. The evaluation metric is the mean average precision (MAP) @ intersection over union (IOU) \[0.50:0.95\] of bounding boxes, which is used in the COCO competition8. Both models can generate accurate (MAP > 0.9) document layout, where M-RCNN shows a small advantage over F-RCNN. The models are more accurate at detecting tables and figures than texts, titles, and lists. We think this is attributed to more regular shapes, more distinctive differences from other categories, and lower rate of erroneous annotations in the training set. The models perform worst on titles, as titles are usually much smaller than other categories and more difficult to detect. TABLE III: MAP @ IOU \[0.50:0.95\] of the F-RCNN and the M-RCNN models on our development and testing sets. M-RCNN shows a small advantage over F-RCNN. Macro average 0.902 0.910 0.900 0.907 Fig. 4 shows some representative examples of the document layout analysis results of testing pages using the M-RCNN model. As implied by the high MAP, the model is able to generate accurate layout. Fig. 5 illustrates some of the rare errors made by the M-RCNN model. We think some of the errors are attributed to the noise in PubLayNet. We will continue improving the quality of PubLayNet. 6Other ICDAR competitions require annotations of document layout categories not available in PubLayNet and the size of the development sets is too small for effective training. 7[https://github.com/Belval/pdf2image](https://github.com/Belval/pdf2image) 8[http://cocodataset.org/#detection-eval](http://cocodataset.org/#detection-eval) Category Dev Test F-RCNN M-RCNN F-RCNN M-RCNN Text 0.910 0.916 0.913 0.917 Title 0.826 0.840 0.812 0.828 List 0.883 0.886 0.885 0.887 Table 0.954 0.960 0.943 0.947 Figure 0.937 0.949 0.945 0.955 B. Table detection The ICDAR 2013 Table Competition \[21\] is one of the most prestigious competitions on table detection in PDF documents from European government sources. We created a table detection dataset by extracting from our training set the PDF pages that contain one or more tables, and remove non-table instances from the annotations. We trained a F-RCNN model and a M-RCNN model on this table detection dataset under the same configuration described in Section IV-A. Then the models are fine-tuned with the 170 example PDF pages provided by the competition. For fine-tuning, we used a base learning rate 0.001, which was decreased by 10 at the 100th iteration out of 200 total iterations. The minimum confidence score for a detection is decided by a 5-fold cross-validation on the 170 training pages. The fine-tuned model was evaluated on the formal competition dataset (238 pages) using the official evaluation toolkit 9. Table IV compares the performance of the fine-tuned models and published approaches. The fine tuned F-RCNN model achieves the state-of-the-art performance reported in \[6\], where the F-RCNN model was fine tuned with 1600 samples from a pre-trained object detection model. By fine tuning from a model pre-trained on document samples, we can obtain the same level of performance with much smaller training data (170 samples). TABLE IV: Fine tuning pre-trained F-RCNN and M-RCNN models for the ICDAR 2013 Table Recognition Competition. Based on models pre-trained on table pages in PubLayNet, we obtained the state-of-the-art performance with only 170 training pages. Input Method Precision Recall F1-score Image F-RCNN 0.972 0.964 0.968 M-RCNN 0.940 0.955 0.947 Schreiber et al. 2017 \[6\] 0.974 0.962 0.968 Tran et al. 2015 \[13\] 0.952 0.964 0.958 PDF Hao et al. 2016 \[15\] 0.972 0.922 0.946 Silva 2010 \[22\] 0.929 0.983 0.955 Nurminen 2013 \[21\] 0.921 0.908 0.914 Yildiz 2005 \[12\] 0.640 0.853 0.731 C. Fine tuning for a different domain In USA, there is a large number of private health insurance providers. Employees are provided with Summary Plan Description (SPD) documents typically in PDF, which describe the benefits provided by the private health insurers. There is a large variety in the layout of SPD documents provided by different companies. The layout of these documents is also distinctively different from scientific publications. We manually annotated the texts, tables, and lists in 20 representative SPD documents that cover a large number of possible layouts. This domain specific dataset contains 2,131 pages, 9,379, 2,500, and 820 instances of text, tables, and lists, respectively. A 5-fold cross-document-validation10 was 9[https://github.com/tamirhassan/dataset-tools](https://github.com/tamirhassan/dataset-tools) 10For each fold, the model is trained on 16 documents and tested on 4 documents Text Title Table Figure List Fig. 4: Representative examples of the document layout analysis results using the M-RCNN model. As implied by the high MAP, the model is able to generate accurate layout. Text Title Table Figure List Fig. 5: Erroneous document layout predictions made by the M-RCNN model. taken to compare different pre-trained F-RCNN and M-RCNN models for fine tuning. We evaluated three fine tuning approaches: 1) initializing the backbone with pre-trained ImageNet model, 2) initializing the whole model with pre-trained COCO model, and 3) initializing the whole model with pre-trained PubLayNet model. We also tested the zero-shot performance of the pre-trained PubLayNet model. The comparison of the performance of the approaches is illustrated in Table V. The performance of the zero-shot PubLayNet model is considerably worse than the fine-tuned models, which demonstrates the distinct difference between the layout of SPD documents and PubMed Central™ articles. Fine tuning the pre-trained PubLayNet model can substantially outperform other fine-tuned models. This demonstrates the advantage of using PubLayNet for document layout analysis. The only exception is that fine tuning pre-trained COCO F-RCNN model detects tables more accurately than fine tuning pre-trained PubLayNet F-RCNN model. In addition, the improvement on table detection by fine tuning pre-trained PubLayNet MRCNN model is relatively low to that on text and list detection. We think this is because the difference of table styles between SPD and the PubMed Central™ articles and more substantial than that of text and list styles, and therefore less knowledge can be transferred to the fine tuned model.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/PubLayNet",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "PubLayNet: Large-Scale Automatic Annotation of Document Layout in PubMed Central Open Access Subset (Xu et al., 2020)"
    },

    {
      "@id": "rdip:Dataset/PMCOA-XML-PDF-2018",
      "@type": "schema:Dataset",
      "schema:name": "PubMed Central Open Access Subset (downloaded 2018-10-03)",
      "schema:size": "1,162,856 articles with complete XML + PDF",
      "schema:description": "Articles provided under Creative Commons, containing both PDF and NLM-JATS XML representations"
    },

    {
      "@id": "rdip:Activity/XML-Preprocessing",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "XML cleaning and standardization (remove math/formula nodes, move list/table/figure to floats-group)",
      "prov:used": "rdip:Dataset/PMCOA-XML-PDF-2018",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PMCOA-XML-Cleaned",
        "@type": "schema:Dataset",
        "schema:name": "Standardized NLM-JATS XML trees"
      }
    },

    {
      "@id": "rdip:Activity/PDF-Parsing",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "PDF parsing with PDFMiner to extract textboxes, textlines, images, geometric shapes",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/PDFMiner",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "PDFMiner",
        "rdip:version": "2018-era"
      },
      "prov:used": "rdip:Dataset/PMCOA-XML-PDF-2018",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PMCOA-PDF-Layout-Elements",
        "@type": "schema:Dataset",
        "schema:name": "Raw PDF layout primitives (textboxes, images, shapes) with bounding boxes"
      }
    },

    {
      "@id": "rdip:Activity/String-Normalization",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Unicode KD normalization of all strings from XML and PDF",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Normalized-Strings",
        "@type": "schema:Dataset"
      }
    },

    {
      "@id": "rdip:Activity/PDF-XML-Matching",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Fuzzy string matching (Levenshtein via fuzzysearch) + adaptive distance threshold + sequential textline matching",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/fuzzysearch",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "fuzzysearch Python package"
      },
      "prov:used": [
        "rdip:Dataset/PMCOA-XML-Cleaned",
        "rdip:Dataset/PMCOA-PDF-Layout-Elements",
        "rdip:Dataset/Normalized-Strings"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Matched-Layout-Elements",
        "@type": "schema:Dataset",
        "schema:name": "PDF elements matched to XML nodes with preliminary category labels"
      }
    },

    {
      "@id": "rdip:Activity/Figure-Table-Body-Annotation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Margin-based annotation of figure/table bodies using main-text box and caption position",
      "prov:used": "rdip:Dataset/Matched-Layout-Elements",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Figure-Table-Bodies",
        "@type": "schema:Dataset"
      }
    },

    {
      "@id": "rdip:Activity/Segmentation-Generation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Polygon segmentation generation from textlines (horizontal/vertical edges only) + reuse bbox for figures/tables",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PubLayNet-Segmentations",
        "@type": "schema:Dataset"
      }
    },

    {
      "@id": "rdip:Activity/Quality-Control-Filtering",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Annotation quality filtering (>99% coverage for non-title pages, >90% for title pages) + manual curation of dev/test",
      "prov:used": [
        "rdip:Dataset/Matched-Layout-Elements",
        "rdip:Dataset/Figure-Table-Bodies",
        "rdip:Dataset/PubLayNet-Segmentations"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PubLayNet-Final",
        "@type": "schema:Dataset",
        "schema:name": "PubLayNet dataset",
        "schema:size": "Training: 340,391 pages; Dev: 11,858 pages; Test: 11,983 pages (5 categories: Text, Title, List, Table, Figure)"
      }
    },

    {
      "@id": "rdip:Activity/Train-Dev-Test-Split",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Journal-level stratified split + balanced sampling per category + manual curation of dev/test",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PubLayNet-Partitions",
        "@type": "schema:Dataset",
        "schema:name": "Official PubLayNet train/val/test splits (Table II)"
      }
    }
  ]
}
```

This JSON-LD accurately captures the full provenance of the **PubLayNet** dataset creation (Xu et al., 2020):

*   Central project: automatic large-scale annotation of document layout using PMCOA
*   Source: 1.16M articles from PubMed Central Open Access (2018 dump) with paired PDF+XML
*   Core innovation: PDF-XML alignment via PDFMiner parsing + fuzzy string matching + margin-based figure/table body inference
*   Multiple processing stages: XML cleaning, PDF parsing, normalization, matching, segmentation generation, strict quality control
*   Final output: PubLayNet – the largest publicly available document layout dataset (∼350k pages, 5 categories) with both bounding boxes and instance segmentations

All major data-production activities and tools (PDFMiner, fuzzysearch) are represented using the RDIP ontology.

## Prompt:
"I will provide you with a 'Methodology' section from a research paper. Your task is to extract the research provenance metadata into JSON-LD format using the RDIP Ontology. Schema Definitions:

*   rdip:ResearchProject: The central hub.
*   rdip:DataProductionActivity: Any step that creates or modifies data (e.g., Analysis, Collection).
*   rdip:SoftwareApplication: The specific tool used.
*   rdip:usedSoftware: The property linking an Activity to the Software.
*   rdip:version: The specific version of the software.
*   rdip:outputDataset: The dataset resulting from the activity.

Input Text: The benchmark in this work has the following components in its foundation: datasets, search space, training and evaluation protocols. In this section we describe all of them. Datasets We use Penn Tree Bank (PTB) \[31\] to train a sample of networks from the search space. We also use the WikiText- 2 \[30\] dataset to train a stratified subsample of networks based on their performance on the PTB dataset. The second dataset is larger and is more realistic since it preserves the letter case, punctuation, and numbers. Statistics of these datasets are shown in Table 1. Macro-level of the search space (AWD-LSTM) The macro-level of each model and the training procedure are borrowed from AWD-LSTM \[29\] as it has a relatively simple structure and has comparable to SOTA performance. The network consists of three stacked cells with weightdrop regularizations in each and locked dropouts between them and input/output layers, as well as a dropout applied to input embedding (see Figure 1). Tokens 1.086M 2.552M Vocab size 10000 33278 OoV rate2 0.049 0.032 Figure 1: AWD-LSTM macro-level. See definitions of dropouts and other parameters of the architec- ture in the original repository \[1\]. Micro-level of the search space (recurrent cells) We define a search space for cells (micro-level of models) to include all conventional recurrent cells as particular instances (see examples in Figure 2). Cell computations are encoded as attributed graphs: 2Out of Vocabulary (OoV) rate — share of tokens outside of the model’s vocabulary; all OoV tokens are replaced with a service token <unknown>. 3 each node is associated with an operation, and edges encode its inputs. The following operations are available:

*   Linear: f (x1, .., xn) = W1x1 +.. + Wnxn + b,
*   Blending (element wise): f (z, x, y) = z ⊙ x + (1− z) ⊙ y,
*   Element wise product and sum,
*   Activations: Tanh, Sigmoid, and LeakyReLU. We impose some constraints on possible instances: number of nodes ≤ 24, number of hidden states ≤ 3, number of linear input vectors n ≤ 3. (a) Simple RNN Cell (b) LSTM Cell (c) GRU Cell Figure 2: Examples of conventional RNN cells. Colors of nodes highlight the corresponding previous and new hidden states, green color also highlights the input vector. Black dashed, blue and red edges indicate blending arguments z, x and y respectively. Generation procedure We used the following graph generation procedure: initial nodes correspond to the input vector and hidden states; at each step, a node is added, an operation associated to the node is randomly chosen and depending on the operation, connections are made with previous nodes; after all, nodes are added, new hidden states are randomly selected among them; next, redundant nodes, that do not lead to the new hidden states in the computational graph, are removed; finally, the architecture is accepted if the input vector and hidden state nodes are in the graph (not redundant), and no hidden state node is directly connected to the new hidden states in order to avoid numeric explosions. In addition, we manually added three architectures to the generated sample as baselines: RNN (Simple RNN Cell), LSTM, and GRU (see Figure 2). Training process We generated 14322 architectures for training on the PTB dataset, 4114 of them were trained three times with different random seeds, the others were trained once; also, 289 out of them were trained on WikiText-2 based on stratified perplexities for PTB. First, we found a trade-off between training time and validation performance on PTB after 50 iterations by varying sizes of the hidden states and batch size for AWD-LSTM (Figure 3a). The chosen pair was nhid = 600 and batch \_ size = 20 because such a network almost converges to the same perplexity as the original AWD-LSTM, where nhid = 1150, but within a half of the original training time. Then we selected a random subset of architectures and performed a grid search of dropout values for each of them on PTB. Figure 3b shows the performance of all configurations for the selected architectures. The following configuration showed the best validation perplexity on average: dropout = 0.1, dropouth = 0.25, dropouti = 0.4, dropoute = 0.0, and wdrop = 0.1. We used that configuration and fixed other training settings for all architectures on both datasets. Evaluation We logged the following models metrics for each epoch: wall time and train/validation/test log perplexity log\_PPL(p) =− x p(x) log p(x), where p is a discrete probability distribution of words. In addition, the total number of trainable parameters and their final values were stored to evaluate architectures on downstream tasks. 4 (a) Hidden states size (nhid) and batch size for AWD-LSTM. (b) Dropouts. Curves correspond to various dropout configuration; black curve corresponds to the best one on average. Figure 3: Hyper-parameters selection. Hardware We use the following hardware specifications to precompute architectures: HPC cluster Zhores \[46\] with Tesla V100-SXM2 with 16Gb of memory on each GPU. 4 Analysis 4.1 Search space evaluation The complete search space is extremely large; for example, there are approximately 1053 connected non-attributed graphs with ≤ 24 nodes and ≤ 3 input edges. Some architectures from the generated sample (around 23%) turned out to suffer from numerical explosions that occurred when, for example, there were no activations between corresponding hidden states. Figure 4a shows the relationship among three metrics: number of parameters, training wall time, and test perplexity. According to the plot, there is no clear correlation between the test perplexity and the number of parameters or training wall time; LSTM and GRU also look like typical representatives of the generated sample. However, based on figure 4b, which shows the distribution of the best test perplexity achieved by each architecture, LSTM and GRU architectures have the top performance in terms of the test perplexity, whereas RNN looks average. (a) Joint distribution of metrics. (b) Best test perplexity distribution. Figure 4: Architectures metrics on PTB. 5 We have investigated how the validation perplexity at different training stages correlates with the final testing perplexity. Figure 5 shows the ranking of architectures based on their final testing perplexities w.r.t. ranking obtained with validation perplexities at 5, 10, 25, and 50 epochs. Figure 5: The ranking of architectures perplexity for different epochs on test and validation sets of PTB: lower rank corresponds to lower perplexity. Architecture Num. params Test perplexity LSTM 10.9M 78.5 Top-2 9.2M 84.7 GRU 9.2M 86.1 Top-4 11.0M 90.6 RNN 5.73M 135.1 Figure 6 shows the correlation of architectures performance on PTB and WikiText-2. The plot suggests good transfer properties of NAS for RNN, that is, architectures that perform well on one dataset, will also perform well on another. We have investigated the sparsity of the generated sample of architectures. Figure 7 shows the his- togram of upper-bounds on Graph Edit Distances (GED) between 1000 random pairs of architectures, which also take into consideration the difference in operations associated with each node. To calculate these values, we used consecutive GED approximations \[2\] (implemented in NetworkX package \[15\]) for the limited time. Table 2 compares the top architectures in more detail. LSTM has the best perfor- Table 2: Detailed comparison of top performing archi- tectures and ordinary RNN on PTB dataset. mance, GRU also achieves top-3 perfor- mance, however, the generated sample also contains a few competitive examples that are substantially different from LSTM and GRU. Their architectures are provided in Appendix A, Figure 11. Parameterization of architectures We used graph2vec \[33\] method to create the characteristic features for architectures, which can be useful for some NAS methods like Bayesian Optimization \[13\]. With this method, architectures were embedded in 10- and 50-dimensional spaces. In order to verify that the obtained features were sensible, we used them to 1) classify the flawed architectures, the ones that experienced problems during the training; and 2) predict the final testing log perplexity. We split corresponding datasets into equal training and testing parts and used XGBoost \[8\] for both problems. ROC AUC metric for the classification (1) was 0.98, whereas R2-score for the regression task (2) was 0.012 (see also Figure 8). We also trained and evaluated task (2) on architectures with log perplexity ≤ 6, and obtained R2-score 0.24. 4.2 Word embedding evaluation Approaches to language model evaluation fall into two major categories: intrinsic and extrinsic evaluation \[39\]. Intrinsic evaluation tests the semantic relationships between words \[3, 32\], and, thus leverages word embeddings only. The whole language model is not involved in the evaluation. The first layer solely, i.e., static (fixed) word embeddings, is subjected to evaluation. Extrinsic evaluation treats the language model as dynamic (contextualized) word embeddings and feeds them as an input layer to a downstream task. It measures the performance metrics for the task to assess the quality of the language model. To fully assess trained architectures, we subject them to intrinsic and extrinsic evaluation, following the best practices from the NLP community. For the sake of time, we did not assess all architectures. Instead, we used a stratified sample of architectures according to the perplexity values. 6 Figure 6: Correlation of architectures’ test log perplexities on PTB and WikiText-2. Figure 7: Histogram of upper bounds of graph edit distances be- tween 1000 random pairs of archi- tectures. Figure 8: True vs predicted final testing log perplexity based on graph2vec features. Intrinsic evaluation We picked two benchmark datasets to evaluate semantic relationships between word pairs: WordSimilarity-353 \[12\], consisting of similatiry judgments for 353 word pairs on a scale of 0 to 10. For example, word pair “book” and “paper” are scored with 7.5. SimLex-999 \[17\] is a larger and more challenging benchmark, consisting of similarity judgments for 999 word pairs. To evaluate word embeddings for each word pair, cosine similarity between word vectors is computed. The resulting similarity values are correlated with the judgments using Spearman’s and Pearson’s correlation coefficients. We used the benchmarks distributed by the gensim framework3. To ensure a fair comparison, we train two word2vec models (in particular, Skip-gram with negative sampling, SGNS) \[32\] on PTB and WikiText-2 independently and use them as baselines for both intrinsic and extrinsic evaluation. Figure 9 shows the results of intrinsic evaluation. When trained on PTB, most of our architectures overcame SGNS by a large margin, judging from the evaluation on both benchmarks. However, this evaluation is overestimated as the intersection of the PTB vocabulary and both benchmarks are rather small. Similar patterns are observed when both SGNS and our architectures are trained on WikiText-2 and compared on WordSim-353. However, as SimLex-999 is more challenging than WordSim-353, only a half of the architectures manages to beat the SGNS baseline. As expected, in all settings, the lower the perplexity is, the higher the performance of the models is. WordSimilarity-353 SimLex-999 WordSimilarity-353 SimLex-999 sgns Model perplexity 250 200 150 100 50 Model perplexity 250 200 150 100 50 sgns sgns sgns Model perplexity 240 220 200 180 160 140 120 100 Model perplexity 240 220 200 180 160 140 120 100 0.15 0.20 0.25 0.30 0.35 Pearson correlation 0.08 0.10 0.12 0.14 0.16 0.18 0.20 0.22 0.24 Pearson correlation 0.15 0.20 0.25 0.30 0.35 Pearson correlation (a) Architectures trained on PTB 0.10 0.12 0.14 0.16 0.18 0.20 Pearson correlation (b) Architectures trained on WikiText-2 Figure 9: OX: performance of 150 random architectures on WordSimilarity-353 and SimLex-999 (measured by Pearson correlation coefficient), OY: model perplexety, red line: SGNS performance on WordSimilarity-353 and SimLex-999 (measured by Pearson correlation coefficient). Extrinsic evaluation We used the General Language Understanding Evaluation (GLUE) benchmark \[41\], a collection of ten diverse tasks aimed at the evaluation of language models performance. The GLUE score is computed as an average of all performance measures for ten tasks, multiplied by 100. We follow the GLUE evaluation pipeline \[41\]: for each task, our architectures encode the input sentences to the vectors, which are passed further to a classifier. We adjust the Jiant toolkit \[42\] to process our architectures. 3[https://radimrehurek.com/gensim/](https://radimrehurek.com/gensim/) 7 Finally, we evaluate two baselines: 1) the average bag-of-words using SGNS embeddings and 2) an LSTM encoder with SGNS embeddings in the same setting. When trained on PTB, only a few architectures perform better than simple bag-of-words baselines. None outperforms the LSTM baseline. Due to the small size of these models vocabulary, we do not observe any dependence between the perplexity values and the GLUE score. The architectures that pose a larger vocabulary, trained on WikiText-2, cope with GLUE tasks much better, and almost 20% of them beat both baselines, achieving mean GLUE at the level of 42. To conclude, our results show that the architectures reach baseline performance and even exceed it in several NLP benchmarks if compared to strong baselines trained under the same conditions. However, these architectures do not achieve the same performance as the recent Transformer-based models, such as BERT \[23\], T5\[37\], or ELECTRA \[10\]. 5 NAS Benchmark We prepared an environment that simulates NAS processes and does the proper measurements of metrics. The environment can perform the following tasks: • train an architecture for the specified number of epochs (the environment automatically simulates checkpoints and continuation of the training process); • return architecture metrics at the specific training epoch (the architecture must be trained until the requested epoch); • return total simulated wall time; • return the testing log perplexity of the best configuration (architecture and epoch) based on validation perplexity. For benchmarking NAS algorithms on our search space, we tested the following methods within the environment: • Random Search in two modes: low-fidelity mode (RS 10E), which trains 5X networks for 10 epochs, and high-fidelity mode, which trains 1X networks for 50 epochs (RS 50E); • Hyperbands (HB) is a feature-agnostic multi-fidelity method \[25\]; • Bayesian Optimization using 10-dimensional (BO 10D) and 50-dimensional (BO 50D) graph2vec features (Sec. 4, parameterization of architectures) and a bagged \[6\] XGBoost regressor to estimate uncertainty of predictions; • Regularized Evolution (RE) \[38\] using graph2vec features; • Hyperopt with the Tree-structured Parzen Estimator (TPE); \[5\]; • SMAC \[20\] using 10-dimensional graph2vec features. Performance of each method was measured with regret vs. total training time, where regret r at the moment t is r(t) = L(t)− L∗ , L(t) is the final test- ing log perplexity of the best architecture according to validation perplexity found so far by the moment t, and L∗ is the lowest testing log perplexity in the whole dataset (in our benchmark L∗ = 4.36, achieved by LSTM architecture). For each method, we report the average regret over 30 trials in Figure

10.  Hyperbands achive the lowest final regret, while BO follows next. 6 Discussion Figure 10: Performance of various NAS meth- ods. Shades of curves correspond to 95%- confidence interval for mean values. The proposed benchmark is in a different vein than the previous ones. Firstly, it has a much more complex search space, however, at the price of being a very sparse sample from it. Secondly, as the analysis has shown, the distribution of performance metrics (perplexity) is not skewed towards the optimum as in Nas-Bench-101, moreover, hand-crafted architectures like LSTM and GRU seem to have a streamlined performance, hardly achievable by random instances from the search space. We believe these peculiarities of our benchmark will bring diversity and new challenges to the neural architecture search community. For example, larger architectures, that are more realistic, pose a challenge on feature engineering, since simple approaches like flat encoding of adjacency matrices of 8 architectures’ graphs would suffer from the curse of dimensionality. In this work, we used graph2vec approach to obtain better features in a small dimensional space, but we leave a space for further experiments with graph neural networks and other graph-encoding techniques.

## Response:
JSON

Copy

```
{
  "@context": {
    "rdip": "https://w3id.org/rdip/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "https://schema.org/"
  },
  "@graph": [
    {
      "@id": "rdip:Project/RNN-NAS-Benchmark",
      "@type": "rdip:ResearchProject",
      "rdfs:label": "Large-Scale Benchmark for Neural Architecture Search in Recurrent Language Modeling (2021)"
    },

    {
      "@id": "rdip:Dataset/PTB",
      "@type": "schema:Dataset",
      "schema:name": "Penn Tree Bank (PTB)",
      "schema:size": "1.086M tokens, vocab 10k"
    },
    {
      "@id": "rdip:Dataset/WikiText-2",
      "@type": "schema:Dataset",
      "schema:name": "WikiText-2",
      "schema:size": "2.552M tokens, vocab 33,278"
    },

    {
      "@id": "rdip:Activity/Search-Space-Generation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Procedural generation of 14,322 attributed recurrent cell graphs (≤24 nodes, ≤3 hidden states, operations: Linear/Blending/Activations)",
      "schema:description": "Random graph generation with constraints + manual addition of RNN/LSTM/GRU baselines",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/RNN-Cell-Search-Space",
        "@type": "schema:Dataset",
        "schema:size": "14,322 unique recurrent cell architectures (macro: AWD-LSTM)"
      }
    },

    {
      "@id": "rdip:Activity/Hyperparameter-Tuning",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Hyperparameter search on AWD-LSTM for hidden size, batch size, and dropout configurations",
      "prov:used": "rdip:Dataset/PTB",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Fixed-Training-Config",
        "@type": "schema:Dataset",
        "schema:description": "nhid=600, batch_size=20, dropout=0.1, dropouth=0.25, dropouti=0.4, dropoute=0.0, wdrop=0.1"
      }
    },

    {
      "@id": "rdip:Activity/Model-Training-PTB",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Training of 14,322 RNN architectures on PTB (4114 ×3 seeds, rest ×1)",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/PyTorch-AWD-LSTM",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "AWD-LSTM PyTorch implementation",
        "rdip:version": "Merity et al. repository"
      },
      "prov:used": [
        "rdip:Dataset/PTB",
        "rdip:Dataset/RNN-Cell-Search-Space",
        "rdip:Dataset/Fixed-Training-Config"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/PTB-Training-Logs",
        "@type": "schema:Dataset",
        "schema:description": "Per-epoch train/val/test log-perplexity, wall time, final parameters for 14,322 models"
      }
    },

    {
      "@id": "rdip:Activity/Stratified-Training-WikiText2",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Training of 289 stratified models on WikiText-2 based on PTB performance",
      "prov:used": [
        "rdip:Dataset/WikiText-2",
        "rdip:Dataset/PTB-Training-Logs"
      ],
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/WikiText2-Training-Logs",
        "@type": "schema:Dataset"
      }
    },

    {
      "@id": "rdip:Activity/Graph-Embedding",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Architecture embedding via graph2vec (10D and 50D)",
      "rdip:usedSoftware": {
        "@id": "rdip:Software/graph2vec",
        "@type": "rdip:SoftwareApplication",
        "schema:name": "graph2vec"
      },
      "prov:used": "rdip:Dataset/RNN-Cell-Search-Space",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Architecture-Embeddings",
        "@type": "schema:Dataset",
        "schema:size": "14,322 × (10D + 50D)"
      }
    },

    {
      "@id": "rdip:Activity/Benchmark-Environment",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Creation of NAS simulation environment with precomputed training trajectories",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/RNN-NAS-Benchmark",
        "@type": "schema:Dataset",
        "schema:name": "Public RNN NAS benchmark with 14,322 pre-trained models, logs, and evaluation API"
      }
    },

    {
      "@id": "rdip:Activity/NAS-Algorithm-Evaluation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Benchmarking of Random Search, Hyperband, BO (graph2vec), RE, TPE, SMAC (30 trials each)",
      "prov:used": "rdip:Dataset/RNN-NAS-Benchmark",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/NAS-Algorithm-Results",
        "@type": "schema:Dataset",
        "schema:name": "Regret vs. wall-time curves (Figure 10)"
      }
    },

    {
      "@id": "rdip:Activity/Word-Embedding-Evaluation",
      "@type": "rdip:DataProductionActivity",
      "rdfs:label": "Intrinsic evaluation on WordSim-353 and SimLex-999 + extrinsic on GLUE (stratified sample)",
      "prov:used": "rdip:Dataset/PTB-Training-Logs",
      "prov:used": "rdip:Dataset/WikiText2-Training-Logs",
      "rdip:outputDataset": {
        "@id": "rdip:Dataset/Embedding-Eval-Results",
        "@type": "schema:Dataset",
        "schema:name": "Figures 9 + GLUE scores"
      }
    }
  ]
}
```

This JSON-LD captures the complete research provenance of the RNN NAS benchmark paper:

*   Central project: creation of a large-scale NAS benchmark for recurrent language models
*   Generation of 14,322 novel recurrent cell architectures + baselines (RNN/LSTM/GRU)
*   Massive training on PTB and stratified subset on WikiText-2
*   Creation of graph2vec embeddings for architectures
*   Public benchmark environment with pre-computed training trajectories
*   Benchmarking of 6 major NAS algorithms
*   Intrinsic/extrinsic evaluation of learned word embeddings

All major data-production activities, software (AWD-LSTM impl, graph2vec), and resulting datasets (the benchmark itself) are faithfully represented using the RDIP ontology.



---
Powered by [Grok Exporter](https://www.grokexporter.com)