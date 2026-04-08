# Search Strategies: EDIA Representation in Canadian Mental Health Pharmacotherapy RCTs

> **Note:** This document was the original search strategy planning document. The methodology evolved during execution: the "top 100 most-cited" selection was replaced with full screening of all 10,904 eligible records. Databases changed from PubMed/Embase/PsycINFO/CINAHL to PubMed/Europe PMC/OpenAlex/Scopus (API-accessible sources). See `04_database_search/search_strategy.md` for the executed methodology and actual results.

## Research Question
Among randomized controlled trials conducted in Canada evaluating pharmacological interventions to prevent, treat, or manage diagnosed mental disorders, what is the representation and reporting of EDIA-related metrics among participants, and how does representation vary across trials and disorders?

## Search Design Rationale
Three concept blocks combined with **AND**:
1. **Mental Disorders** (broad, all DSM-5 categories)
2. **Randomized Controlled Trials / Clinical Trials**
3. **Canada / Canadian**

EDIA/equity/race/ethnicity terms are intentionally **excluded** from the search. The review assesses *whether* trials report these metrics; including equity terms would bias the sample toward trials that already report EDIA data.

**Limits applied across all databases:** English language; publication year 2000-present.

---

## Search Yield Testing (Automated)

| Iteration | Query (abbreviated) | PubMed Count | Action |
|-----------|-------------------|-------------|--------|
| 1 | (Mental Disorders[MeSH] OR psychiatr* OR depress* OR schizophren* OR ...) AND (RCT[pt] OR randomized OR placebo OR ...) AND (Canada[MeSH] OR Canada[tiab] OR Canadian[tiab] OR Ontario OR ...) AND 2000-present AND English | ~10,955 | No narrowing needed — see note below |

**Final PubMed yield estimate: ~10,955 records**

**Important note on yield interpretation:** This yield is expected and appropriate for this study design. The proposal specifies that the **top 100 most-cited trials will be identified via Scopus citation counts**, not by screening all database results. The purpose of these comprehensive search strategies is to:
1. Define the universe of potentially eligible Canadian mental health pharmacotherapy RCTs
2. Validate the Scopus-based identification approach
3. Ensure no highly-cited trials are missed due to database coverage gaps

The high count confirms the search is appropriately sensitive (comprehensive). The citation-count ranking step replaces traditional title/abstract screening as the primary selection mechanism.

### Cross-Database Volume Estimate

| Source | Estimated Count |
|--------|----------------|
| PubMed yield | ~10,955 |
| OpenAlex total (all databases/sources) | ~15,907 |
| Estimated unique records after deduplication | ~12,936 |

Note: The high volume across databases reflects the breadth of the mental disorders concept block (all DSM-5 categories) combined with the sensitivity of the RCT and Canada filters. Since the study selects the top 100 by citation count rather than screening all results, this volume does not represent a screening burden.

---

## Verification of Controlled Vocabulary

The following terms were verified via NLM MeSH Browser, Emtree documentation, and APA Thesaurus resources:

| Term | MeSH (PubMed) | Emtree (Embase) | APA Thesaurus (PsycINFO) | CINAHL Headings |
|------|---------------|-----------------|--------------------------|-----------------|
| Mental disorders (broad) | Mental Disorders [MeSH] (F03) - explode captures all subtypes | mental disease /exp | Mental Disorders (explode) | Mental Disorders (MH, explode) |
| Canada | Canada [MeSH] (Z01.107.567.176) - explode captures all provinces/territories | Canada /exp | -- (use free text) | Canada (MH) |
| RCT publication type | Randomized Controlled Trial [pt] | randomized controlled trial /exp (Emtree) | Treatment Outcome (Clinical Trials as Topic) | Randomized Controlled Trials (MH) |

---

# 1. PubMed Search Strategy

## Concept Table

| Concept | MeSH / Controlled Vocabulary | Free-Text Terms (Title/Abstract) |
|---------|------------------------------|----------------------------------|
| **Mental Disorders** | "Mental Disorders"[MeSH] (exploded - covers all subtypes including depressive, anxiety, psychotic, bipolar, trauma, OCD, ADHD, eating, substance-related, personality, neurodevelopmental, neurocognitive, sleep-wake disorders) | psychiatr*[tiab], mental illness*[tiab], mental disorder*[tiab], mental health[tiab], psychopatholog*[tiab], psychopharmac*[tiab], antidepressant*[tiab], antipsychotic*[tiab], anxiolytic*[tiab], mood stabiliz*[tiab], neuroleptic*[tiab], SSRI[tiab], SNRI[tiab], benzodiazepine*[tiab], lithium[tiab], depress*[tiab], anxiety[tiab], schizophren*[tiab], psychosis[tiab], psychotic[tiab], bipolar[tiab], mania[tiab], manic[tiab], obsessive compulsive[tiab], OCD[tiab], post-traumatic stress[tiab], PTSD[tiab], attention deficit[tiab], ADHD[tiab], anorexia nervosa[tiab], bulimia[tiab], eating disorder*[tiab], substance use disorder*[tiab], substance abuse[tiab], alcohol use disorder*[tiab], opioid use disorder*[tiab], personality disorder*[tiab], borderline personality[tiab], autism spectrum[tiab], insomnia[tiab], panic disorder*[tiab], social anxiety[tiab], phobia*[tiab], generalized anxiety[tiab], major depressive[tiab], dysthymi*[tiab], schizoaffective[tiab], postpartum depress*[tiab], perinatal depress*[tiab] |
| **RCT** | "Randomized Controlled Trial"[pt], "Controlled Clinical Trial"[pt], "Clinical Trials as Topic"[MeSH:noexp], "Random Allocation"[MeSH], "Double-Blind Method"[MeSH], "Single-Blind Method"[MeSH], "Placebos"[MeSH] | randomized[tiab], randomised[tiab], placebo[tiab], randomly[tiab], trial[tiab], groups[tiab], drug therapy[sh] |
| **Canada** | "Canada"[MeSH] (exploded - includes Alberta, British Columbia, Manitoba, New Brunswick, Newfoundland and Labrador, Northwest Territories, Nova Scotia, Nunavut, Ontario, Prince Edward Island, Quebec, Saskatchewan, Yukon Territory) | Canada[tiab], Canadian[tiab], Alberta[tiab], British Columbia[tiab], Manitoba[tiab], New Brunswick[tiab], Newfoundland[tiab], Labrador[tiab], Nova Scotia[tiab], Ontario[tiab], Quebec[tiab], Saskatchewan[tiab], Prince Edward Island[tiab], Northwest Territories[tiab], Nunavut[tiab], Yukon[tiab], Toronto[tiab], Montreal[tiab], Vancouver[tiab], Ottawa[tiab], Calgary[tiab], Edmonton[tiab], Winnipeg[tiab], Halifax[tiab], Victoria BC[tiab], Hamilton Ontario[tiab], Quebec City[tiab], Mississauga[tiab], Surrey BC[tiab], London Ontario[tiab], Saskatoon[tiab], Regina[tiab], Sherbrooke[tiab], St. John*[tiab], Fredericton[tiab], Charlottetown[tiab], Whitehorse[tiab], Yellowknife[tiab], Iqaluit[tiab], Kingston Ontario[tiab], Thunder Bay[tiab], Sudbury Ontario[tiab] |
| **Canada (Affiliations)** | -- | Canada[ad], Canadian[ad], Alberta[ad], British Columbia[ad], Manitoba[ad], Ontario[ad], Quebec[ad], Saskatchewan[ad], Nova Scotia[ad], Newfoundland[ad], Toronto[ad], Montreal[ad], Vancouver[ad], Ottawa[ad], Calgary[ad], Edmonton[ad], Winnipeg[ad], Halifax[ad], Hamilton[ad] |

## Line-Numbered Search Strategy

```
# CONCEPT 1: MENTAL DISORDERS
#1  "Mental Disorders"[MeSH]
#2  psychiatr*[tiab] OR "mental illness"[tiab] OR "mental illnesses"[tiab] OR "mental disorder"[tiab] OR "mental disorders"[tiab] OR "mental health"[tiab] OR psychopatholog*[tiab]
#3  psychopharmac*[tiab] OR antidepressant*[tiab] OR antipsychotic*[tiab] OR anxiolytic*[tiab] OR "mood stabiliz*"[tiab] OR neuroleptic*[tiab] OR SSRI[tiab] OR SNRI[tiab] OR benzodiazepine*[tiab] OR lithium[tiab]
#4  depress*[tiab] OR "major depressive"[tiab] OR dysthymi*[tiab] OR "postpartum depression"[tiab] OR "perinatal depression"[tiab]
#5  anxiety[tiab] OR "panic disorder"[tiab] OR "social anxiety"[tiab] OR phobia*[tiab] OR "generalized anxiety"[tiab] OR agoraphobia[tiab]
#6  schizophren*[tiab] OR psychosis[tiab] OR psychotic[tiab] OR schizoaffective[tiab]
#7  bipolar[tiab] OR mania[tiab] OR manic[tiab] OR "mood disorder"[tiab] OR "mood disorders"[tiab]
#8  "obsessive compulsive"[tiab] OR OCD[tiab]
#9  "post-traumatic stress"[tiab] OR "posttraumatic stress"[tiab] OR PTSD[tiab]
#10 "attention deficit"[tiab] OR ADHD[tiab]
#11 "anorexia nervosa"[tiab] OR bulimia[tiab] OR "eating disorder"[tiab] OR "eating disorders"[tiab] OR "binge eating"[tiab]
#12 "substance use disorder"[tiab] OR "substance abuse"[tiab] OR "alcohol use disorder"[tiab] OR "opioid use disorder"[tiab] OR "drug dependence"[tiab] OR "alcohol dependence"[tiab] OR "opioid dependence"[tiab]
#13 "personality disorder"[tiab] OR "personality disorders"[tiab] OR "borderline personality"[tiab]
#14 "autism spectrum"[tiab] OR autistic[tiab]
#15 insomnia[tiab] OR "sleep-wake disorder"[tiab] OR "sleep disorder"[tiab]
#16 "neurocognitive disorder"[tiab] OR dementia[tiab] OR "Alzheimer*"[tiab]
#17 #1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16

# CONCEPT 2: RCT FILTER (Cochrane Highly Sensitive Search Strategy - Sensitivity Maximizing Version, 2008 Revision)
#18 "Randomized Controlled Trial"[pt]
#19 "Controlled Clinical Trial"[pt]
#20 randomized[tiab]
#21 placebo[tiab]
#22 "drug therapy"[sh]
#23 randomly[tiab]
#24 trial[tiab]
#25 groups[tiab]
#26 #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25
#27 "Animals"[MeSH] NOT "Humans"[MeSH]
#28 #26 NOT #27

# CONCEPT 3: CANADA
#29 "Canada"[MeSH]
#30 Canada[tiab] OR Canadian[tiab] OR Canadians[tiab]
#31 Alberta[tiab] OR "British Columbia"[tiab] OR Manitoba[tiab] OR "New Brunswick"[tiab] OR Newfoundland[tiab] OR Labrador[tiab] OR "Nova Scotia"[tiab] OR Ontario[tiab] OR Quebec[tiab] OR Saskatchewan[tiab] OR "Prince Edward Island"[tiab] OR "Northwest Territories"[tiab] OR Nunavut[tiab] OR Yukon[tiab]
#32 Toronto[tiab] OR Montreal[tiab] OR Vancouver[tiab] OR Ottawa[tiab] OR Calgary[tiab] OR Edmonton[tiab] OR Winnipeg[tiab] OR Halifax[tiab] OR Hamilton[tiab] OR Mississauga[tiab] OR Saskatoon[tiab] OR Regina[tiab] OR Sherbrooke[tiab] OR Fredericton[tiab] OR Charlottetown[tiab] OR Whitehorse[tiab] OR Yellowknife[tiab] OR Iqaluit[tiab] OR "Thunder Bay"[tiab] OR "Quebec City"[tiab] OR Kingston[tiab] OR Sudbury[tiab] OR "St. John"[tiab]
#33 Canada[ad] OR Canadian[ad] OR Alberta[ad] OR "British Columbia"[ad] OR Manitoba[ad] OR Ontario[ad] OR Quebec[ad] OR Saskatchewan[ad] OR "Nova Scotia"[ad] OR Newfoundland[ad] OR Toronto[ad] OR Montreal[ad] OR Vancouver[ad] OR Ottawa[ad] OR Calgary[ad] OR Edmonton[ad] OR Winnipeg[ad] OR Halifax[ad] OR Hamilton[ad]
#34 #29 OR #30 OR #31 OR #32 OR #33

# COMBINE AND APPLY LIMITS
#35 #17 AND #28 AND #34
#36 #35 AND ("2000/01/01"[PDAT] : "3000/12/31"[PDAT])
#37 #36 AND English[la]
```

## Syntax Notes (PubMed)
- `[MeSH]` = Medical Subject Heading (auto-exploded in PubMed)
- `[pt]` = Publication Type
- `[tiab]` = Title/Abstract
- `[sh]` = MeSH Subheading
- `[ad]` = Affiliation field (captures institutional addresses)
- `[la]` = Language
- `[PDAT]` = Publication Date
- `*` = Truncation (right-hand wildcard)
- PubMed auto-explodes MeSH terms, so "Mental Disorders"[MeSH] retrieves all narrower terms in the F03 tree
- "Canada"[MeSH] auto-explodes to include all provinces and territories
- The affiliation field [ad] is searched to capture trials with Canadian institutional leadership even when Canada is not in the title/abstract
- The Cochrane Highly Sensitive Search Strategy (sensitivity-maximizing version, 2008 revision) is used for the RCT concept block

---

# 2. Embase (Ovid) Search Strategy

## Concept Table

| Concept | Emtree (Controlled Vocabulary) | Free-Text Terms |
|---------|-------------------------------|-----------------|
| **Mental Disorders** | exp mental disease/ (exploded - covers all subtypes) | psychiatr*.mp., mental illness*.mp., mental disorder*.mp., psychopatholog*.mp., psychopharmac*.mp., antidepressant*.mp., antipsychotic*.mp., anxiolytic*.mp., mood stabiliz*.mp., neuroleptic*.mp., SSRI.mp., SNRI.mp., benzodiazepine*.mp., lithium.mp., depress*.ti,ab., schizophren*.ti,ab., bipolar.ti,ab., anxiety.ti,ab., psychosis.ti,ab., PTSD.ti,ab., OCD.ti,ab., ADHD.ti,ab., eating disorder*.ti,ab., substance use disorder*.ti,ab., personality disorder*.ti,ab. |
| **RCT** | exp randomized controlled trial/ , exp clinical trial/ , crossover procedure/ , double-blind procedure/ , single-blind procedure/ , random*.mp. | randomized.tw., randomised.tw., placebo.tw., double-blind*.tw., single-blind*.tw., factorial*.tw., crossover*.tw., cross over*.tw., assign*.tw., allocat*.tw., volunteer*.tw., trial.tw. |
| **Canada** | exp Canada/ (exploded - covers all provinces/territories) | Canada.mp., Canadian*.mp., Alberta.mp., British Columbia.mp., Ontario.mp., Quebec.mp., Manitoba.mp., Saskatchewan.mp., Nova Scotia.mp., New Brunswick.mp., Newfoundland.mp., Prince Edward Island.mp., Northwest Territories.mp., Nunavut.mp., Yukon.mp., Toronto.mp., Montreal.mp., Vancouver.mp., Ottawa.mp., Calgary.mp., Edmonton.mp., Winnipeg.mp., Halifax.mp., Hamilton.mp. |

## Line-Numbered Search Strategy

```
# CONCEPT 1: MENTAL DISORDERS
1  exp mental disease/
2  psychiatr*.ti,ab.
3  (mental illness* or mental disorder* or mental health or psychopatholog*).ti,ab.
4  (psychopharmac* or antidepressant* or antipsychotic* or anxiolytic* or mood stabiliz* or neuroleptic*).ti,ab.
5  (SSRI or SNRI or benzodiazepine* or lithium).ti,ab.
6  (depress* or major depressive or dysthymi* or postpartum depression or perinatal depression).ti,ab.
7  (anxiety or panic disorder* or social anxiety or phobia* or generalized anxiety or agoraphobia).ti,ab.
8  (schizophren* or psychosis or psychotic or schizoaffective).ti,ab.
9  (bipolar or mania or manic or mood disorder*).ti,ab.
10 (obsessive compulsive or OCD).ti,ab.
11 (post-traumatic stress or posttraumatic stress or PTSD).ti,ab.
12 (attention deficit or ADHD).ti,ab.
13 (anorexia nervosa or bulimia or eating disorder* or binge eating).ti,ab.
14 (substance use disorder* or substance abuse or alcohol use disorder* or opioid use disorder* or drug dependence or alcohol dependence or opioid dependence).ti,ab.
15 (personality disorder* or borderline personality).ti,ab.
16 (autism spectrum or autistic).ti,ab.
17 (insomnia or sleep-wake disorder* or sleep disorder*).ti,ab.
18 (neurocognitive disorder* or dementia or Alzheimer*).ti,ab.
19 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18

# CONCEPT 2: RCT FILTER (Cochrane Embase RCT Filter - Ovid, Sensitivity Maximizing)
20 exp randomized controlled trial/
21 exp controlled clinical trial/
22 (randomized or randomised).tw.
23 placebo.tw.
24 *clinical trial/
25 randomly.tw.
26 trial.ti.
27 exp crossover procedure/
28 exp double-blind procedure/
29 exp single-blind procedure/
30 (crossover* or cross over*).tw.
31 (double blind* or doubleblind*).tw.
32 (single blind* or singleblind*).tw.
33 assign*.tw.
34 allocat*.tw.
35 volunteer*.tw.
36 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35
37 exp animal/ not exp human/
38 36 not 37

# CONCEPT 3: CANADA
39 exp Canada/
40 (Canada or Canadian or Canadians).ti,ab.
41 (Alberta or British Columbia or Manitoba or New Brunswick or Newfoundland or Labrador or Nova Scotia or Ontario or Quebec or Saskatchewan or Prince Edward Island or Northwest Territories or Nunavut or Yukon).ti,ab.
42 (Toronto or Montreal or Vancouver or Ottawa or Calgary or Edmonton or Winnipeg or Halifax or Hamilton or Mississauga or Saskatoon or Regina or Sherbrooke or Fredericton or Charlottetown or Whitehorse or Yellowknife or Iqaluit or Thunder Bay or Quebec City or Kingston or Sudbury or St. John*).ti,ab.
43 (Canada or Canadian or Alberta or British Columbia or Ontario or Quebec or Manitoba or Saskatchewan or Nova Scotia or Newfoundland or Toronto or Montreal or Vancouver or Ottawa or Calgary or Edmonton or Winnipeg or Halifax or Hamilton).in.
44 39 or 40 or 41 or 42 or 43

# COMBINE AND APPLY LIMITS
45 19 and 38 and 44
46 limit 45 to yr="2000-Current"
47 limit 46 to english language
```

## Syntax Notes (Embase/Ovid)
- `exp` = Explode (retrieves term and all narrower terms in the Emtree hierarchy)
- `/` after a term = Emtree subject heading
- `*` before a heading = Focus (major concept); after text = truncation
- `.ti,ab.` = Title and Abstract fields
- `.tw.` = Text Word (title, abstract, and other text fields)
- `.mp.` = Multi-Purpose (title, abstract, heading word, drug trade name, original title, device manufacturer, device trade name, keyword, floating subheading word, candidate term word)
- `.in.` = Institution/Affiliation field
- `exp mental disease/` is the Emtree equivalent of MeSH "Mental Disorders" and covers all psychiatric conditions when exploded
- The Cochrane Embase RCT filter (sensitivity-maximizing version) is adapted for this search
- The `.in.` field captures Canadian institutional affiliations

---

# 3. PsycINFO (Ovid) Search Strategy

## Concept Table

| Concept | APA Thesaurus (Controlled Vocabulary) | Free-Text Terms |
|---------|--------------------------------------|-----------------|
| **Mental Disorders** | exp Mental Disorders/ (exploded - covers all subtypes in APA Thesaurus hierarchy) | psychiatr*.ti,ab., mental illness*.ti,ab., mental disorder*.ti,ab., psychopharmac*.ti,ab., antidepressant*.ti,ab., antipsychotic*.ti,ab., anxiolytic*.ti,ab., mood stabiliz*.ti,ab., neuroleptic*.ti,ab., SSRI.ti,ab., SNRI.ti,ab., benzodiazepine*.ti,ab., depress*.ti,ab., schizophren*.ti,ab., bipolar.ti,ab., anxiety.ti,ab., psychosis.ti,ab., PTSD.ti,ab., OCD.ti,ab., ADHD.ti,ab., eating disorder*.ti,ab., substance use disorder*.ti,ab., personality disorder*.ti,ab. |
| **RCT** | exp Clinical Trials/ , Treatment Effectiveness Evaluation/ , Placebo/ , exp Drug Therapy/ | randomized.tw., randomised.tw., placebo.tw., randomly.tw., trial.tw., clinical trial*.tw., double-blind*.tw., single-blind*.tw., controlled trial*.tw., random* allocat*.tw., crossover*.tw. |
| **Canada** | -- (PsycINFO does not have a geographic thesaurus; use free text and location fields) | Canada.mp., Canadian*.mp., province/territory names.mp., city names.mp., Canada.lo. (location field) |

## Line-Numbered Search Strategy

```
# CONCEPT 1: MENTAL DISORDERS
1  exp Mental Disorders/
2  psychiatr*.ti,ab.
3  (mental illness* or mental disorder* or mental health or psychopatholog*).ti,ab.
4  (psychopharmac* or antidepressant* or antipsychotic* or anxiolytic* or mood stabiliz* or neuroleptic*).ti,ab.
5  (SSRI or SNRI or benzodiazepine* or lithium).ti,ab.
6  (depress* or major depressive or dysthymi* or postpartum depression or perinatal depression).ti,ab.
7  (anxiety or panic disorder* or social anxiety or phobia* or generalized anxiety or agoraphobia).ti,ab.
8  (schizophren* or psychosis or psychotic or schizoaffective).ti,ab.
9  (bipolar or mania or manic or mood disorder*).ti,ab.
10 (obsessive compulsive or OCD).ti,ab.
11 (post-traumatic stress or posttraumatic stress or PTSD).ti,ab.
12 (attention deficit or ADHD).ti,ab.
13 (anorexia nervosa or bulimia or eating disorder* or binge eating).ti,ab.
14 (substance use disorder* or substance abuse or alcohol use disorder* or opioid use disorder* or drug dependence or alcohol dependence or opioid dependence).ti,ab.
15 (personality disorder* or borderline personality).ti,ab.
16 (autism spectrum or autistic).ti,ab.
17 (insomnia or sleep-wake disorder* or sleep disorder*).ti,ab.
18 (neurocognitive disorder* or dementia or Alzheimer*).ti,ab.
19 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18

# CONCEPT 2: RCT FILTER (Adapted for PsycINFO)
20 exp Clinical Trials/
21 Treatment Effectiveness Evaluation/
22 Placebo/
23 exp Drug Therapy/
24 (randomized or randomised).tw.
25 placebo*.tw.
26 randomly.tw.
27 (clinical trial* or controlled trial*).tw.
28 (double blind* or doubleblind* or double-blind*).tw.
29 (single blind* or singleblind* or single-blind*).tw.
30 (random* adj2 (assign* or allocat*)).tw.
31 (crossover* or cross over*).tw.
32 trial.ti.
33 groups.tw.
34 20 or 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33

# CONCEPT 3: CANADA
35 (Canada or Canadian or Canadians).ti,ab.
36 (Alberta or British Columbia or Manitoba or New Brunswick or Newfoundland or Labrador or Nova Scotia or Ontario or Quebec or Saskatchewan or Prince Edward Island or Northwest Territories or Nunavut or Yukon).ti,ab.
37 (Toronto or Montreal or Vancouver or Ottawa or Calgary or Edmonton or Winnipeg or Halifax or Hamilton or Mississauga or Saskatoon or Regina or Sherbrooke or Fredericton or Charlottetown or Whitehorse or Yellowknife or Iqaluit or Thunder Bay or Quebec City or Kingston or Sudbury or St. John*).ti,ab.
38 (Canada or Canadian or Alberta or British Columbia or Ontario or Quebec or Manitoba or Saskatchewan or Nova Scotia or Newfoundland or Toronto or Montreal or Vancouver or Ottawa or Calgary or Edmonton or Winnipeg or Halifax or Hamilton).in.
39 35 or 36 or 37 or 38

# COMBINE AND APPLY LIMITS
40 19 and 34 and 39
41 limit 40 to yr="2000-Current"
42 limit 41 to english language
```

## Syntax Notes (PsycINFO/Ovid)
- `exp` = Explode (retrieves term and all narrower terms in the APA Thesaurus hierarchy)
- `/` after a term = APA Thesaurus descriptor
- `.ti,ab.` = Title and Abstract fields
- `.tw.` = Text Word
- `.mp.` = Multi-Purpose field
- `.in.` = Institution/Affiliation field
- `adj2` = Adjacency operator (terms within 2 words of each other, in any order)
- PsycINFO does not have a geographic thesaurus, so Canada is captured entirely through free-text searching and the institution field
- `exp Mental Disorders/` in PsycINFO covers the full hierarchy of psychiatric diagnoses in the APA Thesaurus
- `exp Drug Therapy/` is included to capture pharmacological intervention studies
- PsycINFO auto-explodes thesaurus terms; the `exp` is included for clarity and to ensure narrower terms are captured

---

# 4. CINAHL (EBSCO) Search Strategy

## Concept Table

| Concept | CINAHL Subject Headings (MH) | Free-Text Terms (TX / TI / AB) |
|---------|------------------------------|-------------------------------|
| **Mental Disorders** | (MH "Mental Disorders+") (exploded with +) | TI/AB: psychiatr*, mental illness*, mental disorder*, psychopharmac*, antidepressant*, antipsychotic*, anxiolytic*, mood stabiliz*, neuroleptic*, SSRI, SNRI, benzodiazepine*, depress*, schizophren*, bipolar, anxiety, psychosis, PTSD, OCD, ADHD, eating disorder*, substance use disorder*, personality disorder* |
| **RCT** | (MH "Randomized Controlled Trials+"), (MH "Clinical Trials+"), (MH "Placebos"), (MH "Random Assignment"), (MH "Double-Blind Studies"), (MH "Single-Blind Studies"), (MH "Triple-Blind Studies") | TI/AB: randomized, randomised, placebo, randomly, trial, clinical trial*, controlled trial*, double-blind*, single-blind*, crossover*, random* allocat*, random* assign* |
| **Canada** | (MH "Canada+") (exploded with +) | TI/AB: Canada, Canadian, province names, city names; AF (affiliation): Canada, Canadian, major provinces/cities |

## Line-Numbered Search Strategy

```
# CONCEPT 1: MENTAL DISORDERS
S1  (MH "Mental Disorders+")
S2  TI ( psychiatr* OR "mental illness" OR "mental illnesses" OR "mental disorder" OR "mental disorders" OR "mental health" OR psychopatholog* ) OR AB ( psychiatr* OR "mental illness" OR "mental illnesses" OR "mental disorder" OR "mental disorders" OR "mental health" OR psychopatholog* )
S3  TI ( psychopharmac* OR antidepressant* OR antipsychotic* OR anxiolytic* OR "mood stabiliz*" OR neuroleptic* OR SSRI OR SNRI OR benzodiazepine* OR lithium ) OR AB ( psychopharmac* OR antidepressant* OR antipsychotic* OR anxiolytic* OR "mood stabiliz*" OR neuroleptic* OR SSRI OR SNRI OR benzodiazepine* OR lithium )
S4  TI ( depress* OR "major depressive" OR dysthymi* OR "postpartum depression" OR "perinatal depression" ) OR AB ( depress* OR "major depressive" OR dysthymi* OR "postpartum depression" OR "perinatal depression" )
S5  TI ( anxiety OR "panic disorder*" OR "social anxiety" OR phobia* OR "generalized anxiety" OR agoraphobia ) OR AB ( anxiety OR "panic disorder*" OR "social anxiety" OR phobia* OR "generalized anxiety" OR agoraphobia )
S6  TI ( schizophren* OR psychosis OR psychotic OR schizoaffective ) OR AB ( schizophren* OR psychosis OR psychotic OR schizoaffective )
S7  TI ( bipolar OR mania OR manic OR "mood disorder*" ) OR AB ( bipolar OR mania OR manic OR "mood disorder*" )
S8  TI ( "obsessive compulsive" OR OCD ) OR AB ( "obsessive compulsive" OR OCD )
S9  TI ( "post-traumatic stress" OR "posttraumatic stress" OR PTSD ) OR AB ( "post-traumatic stress" OR "posttraumatic stress" OR PTSD )
S10 TI ( "attention deficit" OR ADHD ) OR AB ( "attention deficit" OR ADHD )
S11 TI ( "anorexia nervosa" OR bulimia OR "eating disorder*" OR "binge eating" ) OR AB ( "anorexia nervosa" OR bulimia OR "eating disorder*" OR "binge eating" )
S12 TI ( "substance use disorder*" OR "substance abuse" OR "alcohol use disorder*" OR "opioid use disorder*" OR "drug dependence" OR "alcohol dependence" OR "opioid dependence" ) OR AB ( "substance use disorder*" OR "substance abuse" OR "alcohol use disorder*" OR "opioid use disorder*" OR "drug dependence" OR "alcohol dependence" OR "opioid dependence" )
S13 TI ( "personality disorder*" OR "borderline personality" ) OR AB ( "personality disorder*" OR "borderline personality" )
S14 TI ( "autism spectrum" OR autistic ) OR AB ( "autism spectrum" OR autistic )
S15 TI ( insomnia OR "sleep-wake disorder*" OR "sleep disorder*" ) OR AB ( insomnia OR "sleep-wake disorder*" OR "sleep disorder*" )
S16 TI ( "neurocognitive disorder*" OR dementia OR Alzheimer* ) OR AB ( "neurocognitive disorder*" OR dementia OR Alzheimer* )
S17 S1 OR S2 OR S3 OR S4 OR S5 OR S6 OR S7 OR S8 OR S9 OR S10 OR S11 OR S12 OR S13 OR S14 OR S15 OR S16

# CONCEPT 2: RCT FILTER
S18 (MH "Randomized Controlled Trials+")
S19 (MH "Clinical Trials+")
S20 (MH "Placebos")
S21 (MH "Random Assignment")
S22 (MH "Double-Blind Studies")
S23 (MH "Single-Blind Studies")
S24 (MH "Triple-Blind Studies")
S25 TI ( randomized OR randomised ) OR AB ( randomized OR randomised )
S26 TI placebo* OR AB placebo*
S27 TI randomly OR AB randomly
S28 TI ( "clinical trial*" OR "controlled trial*" ) OR AB ( "clinical trial*" OR "controlled trial*" )
S29 TI ( "double blind*" OR "single blind*" OR "triple blind*" ) OR AB ( "double blind*" OR "single blind*" OR "triple blind*" )
S30 TI ( crossover* OR "cross over*" ) OR AB ( crossover* OR "cross over*" )
S31 TI ( random* N2 allocat* ) OR AB ( random* N2 allocat* )
S32 TI ( random* N2 assign* ) OR AB ( random* N2 assign* )
S33 TI trial
S34 S18 OR S19 OR S20 OR S21 OR S22 OR S23 OR S24 OR S25 OR S26 OR S27 OR S28 OR S29 OR S30 OR S31 OR S32 OR S33

# CONCEPT 3: CANADA
S35 (MH "Canada+")
S36 TI ( Canada OR Canadian OR Canadians ) OR AB ( Canada OR Canadian OR Canadians )
S37 TI ( Alberta OR "British Columbia" OR Manitoba OR "New Brunswick" OR Newfoundland OR Labrador OR "Nova Scotia" OR Ontario OR Quebec OR Saskatchewan OR "Prince Edward Island" OR "Northwest Territories" OR Nunavut OR Yukon ) OR AB ( Alberta OR "British Columbia" OR Manitoba OR "New Brunswick" OR Newfoundland OR Labrador OR "Nova Scotia" OR Ontario OR Quebec OR Saskatchewan OR "Prince Edward Island" OR "Northwest Territories" OR Nunavut OR Yukon )
S38 TI ( Toronto OR Montreal OR Vancouver OR Ottawa OR Calgary OR Edmonton OR Winnipeg OR Halifax OR Hamilton OR Mississauga OR Saskatoon OR Regina OR Sherbrooke OR Fredericton OR Charlottetown OR Whitehorse OR Yellowknife OR Iqaluit OR "Thunder Bay" OR "Quebec City" OR Kingston OR Sudbury OR "St. John*" ) OR AB ( Toronto OR Montreal OR Vancouver OR Ottawa OR Calgary OR Edmonton OR Winnipeg OR Halifax OR Hamilton OR Mississauga OR Saskatoon OR Regina OR Sherbrooke OR Fredericton OR Charlottetown OR Whitehorse OR Yellowknife OR Iqaluit OR "Thunder Bay" OR "Quebec City" OR Kingston OR Sudbury OR "St. John*" )
S39 AF ( Canada OR Canadian OR Alberta OR "British Columbia" OR Ontario OR Quebec OR Manitoba OR Saskatchewan OR "Nova Scotia" OR Newfoundland OR Toronto OR Montreal OR Vancouver OR Ottawa OR Calgary OR Edmonton OR Winnipeg OR Halifax OR Hamilton )
S40 S35 OR S36 OR S37 OR S38 OR S39

# COMBINE AND APPLY LIMITS
S41 S17 AND S34 AND S40

# Apply limiters via EBSCO interface:
# - Publication Date: 2000-01 to 2026-12
# - Language: English
S42 S41 [Limiters - Published Date: 20000101-20261231; Language: English]
```

## Syntax Notes (CINAHL/EBSCO)
- `MH` = CINAHL Subject Heading (equivalent to MeSH)
- `+` after a heading = Explode (includes all narrower terms)
- `TI` = Title field
- `AB` = Abstract field
- `TX` = All Text (broader than TI/AB; not used here to maintain precision)
- `AF` = Affiliation field
- `N2` = Near operator (terms within 2 words of each other, in any order) -- CINAHL/EBSCO proximity operator
- `*` = Truncation
- `S` prefix = Search line number (EBSCO convention)
- CINAHL subject headings follow the MeSH structure closely; "Mental Disorders+" explodes to capture all psychiatric subtypes
- Date and language limits are applied via EBSCO interface limiters or can be combined with Boolean operators
- The AF (affiliation) field captures Canadian institutional addresses

---

# Summary of Filters Applied

| Database | Date Filter | Language Filter | RCT Filter Source |
|----------|------------|----------------|-------------------|
| PubMed | 2000/01/01 to present ([PDAT]) | English [la] | Cochrane HSS, Sensitivity-Maximizing (2008 revision) |
| Embase (Ovid) | yr="2000-Current" (limit command) | English language (limit command) | Cochrane Embase RCT Filter, Sensitivity-Maximizing |
| PsycINFO (Ovid) | yr="2000-Current" (limit command) | English language (limit command) | Adapted RCT filter (APA Thesaurus terms + free text) |
| CINAHL (EBSCO) | Published Date: 20000101-20261231 | English (limiter) | CINAHL subject headings + free-text RCT terms |

---

# Notes for the Review Team

1. **No EDIA terms in the search.** The search is designed to retrieve ALL Canadian mental health pharmacotherapy RCTs. EDIA assessment (race, ethnicity, sex, gender, socioeconomic status, language, disability, Indigeneity, immigration status) occurs at the data extraction stage.

2. **Sensitivity over specificity.** The strategies err on the side of inclusiveness. The mental disorders block uses both the broad exploded MeSH/Emtree heading AND extensive free-text terms. The Canada block searches title/abstract, affiliation fields, AND controlled vocabulary.

3. **Affiliation field searching.** Lines searching the affiliation/institution field (PubMed [ad], Embase .in., PsycINFO .in., CINAHL AF) capture trials with Canadian institutional leadership even when "Canada" does not appear in the title or abstract. This is critical for multi-site international trials with a Canadian arm.

4. **City names may generate false positives.** Some city names (Hamilton, London, Kingston, Victoria, Regina, St. John) exist in other countries. The affiliation field search and AND-combination with mental disorders and RCT concepts will minimize irrelevant results, but screening should be aware of this.

5. **Deduplication.** Results from all four databases should be imported into a reference manager (e.g., Covidence, EndNote) and deduplicated before screening.

6. **Top 100 most-cited.** After deduplication, citation counts can be obtained from Web of Science, Scopus, or Google Scholar to rank and select the top 100 most-cited trials for full analysis.

7. **Date of search.** Record the exact date the search is run in each database for PRISMA reporting.
