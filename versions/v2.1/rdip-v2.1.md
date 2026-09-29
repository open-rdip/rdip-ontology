## Ontology Diagram

```mermaid
graph LR
    classDef project fill:#ffff99,stroke:#333,color:#000000;
    classDef activity fill:#ffcc99,stroke:#333,color:#000000;
    classDef person fill:#99ff99,stroke:#333,color:#000000;
    classDef org fill:#99ccff,stroke:#333,color:#000000;
    classDef software fill:#ff99cc,stroke:#333,color:#000000;
    classDef dataset fill:#ccff99,stroke:#333,color:#000000;
    classDef method fill:#99ffff,stroke:#333,color:#000000;
    classDef role fill:#ff9999,stroke:#333,color:#000000;
    classDef article fill:#cccccc,stroke:#333,color:#000000;
    classDef param fill:#9999ff,stroke:#333,color:#000000;
    classDef env fill:#ffccff,stroke:#333,color:#000000;
    classDef result fill:#cc99ff,stroke:#333,color:#000000;
    classDef recipe fill:#ffd699,stroke:#333,color:#000000;

    %% ── PROJECT ──
    ResearchProject["ResearchProject </br> rdip:ResearchProject </br> ≡ schema:Project | ⊑ prov:Entity"]:::project

    %% ── ACTIVITY HIERARCHY ──
    ResearchActivity["ResearchActivity </br> rdip:ResearchActivity </br> ⊑ prov:Activity, schema:Action"]:::activity
    PlanningActivity["PlanningActivity </br> rdip:PlanningActivity"]:::activity
    DataCollectionActivity["DataCollectionActivity </br> rdip:DataCollectionActivity"]:::activity
    DataProductionActivity["DataProductionActivity </br> rdip:DataProductionActivity"]:::activity
    DataProcessingActivity["DataProcessingActivity </br> rdip:DataProcessingActivity"]:::activity
    DataAnalysisActivity["DataAnalysisActivity </br> rdip:DataAnalysisActivity"]:::activity
    DataPublishingActivity["DataPublishingActivity </br> rdip:DataPublishingActivity"]:::activity
    DataPreservationActivity["DataPreservationActivity </br> rdip:DataPreservationActivity"]:::activity
    PublicationActivity["PublicationActivity </br> rdip:PublicationActivity"]:::activity
    SoftwareDevelopmentActivity["SoftwareDevelopmentActivity </br> rdip:SoftwareDevelopmentActivity"]:::activity

    %% ── SUBCLASS HIERARCHY — ACTIVITIES ──
    ResearchActivity -- subClassOf --> PlanningActivity
    ResearchActivity -- subClassOf --> DataCollectionActivity
    ResearchActivity -- subClassOf --> DataProductionActivity
    ResearchActivity -- subClassOf --> DataProcessingActivity
    ResearchActivity -- subClassOf --> DataAnalysisActivity
    ResearchActivity -- subClassOf --> DataPublishingActivity
    ResearchActivity -- subClassOf --> DataPreservationActivity
    ResearchActivity -- subClassOf --> PublicationActivity
    ResearchActivity -- subClassOf --> SoftwareDevelopmentActivity

    %% ── PEOPLE & ROLES ──
    Person["Person </br> vivo:Person </br> ≡ schema:Person"]:::person
    Organization["Organization </br> vivo:Organization </br> ≡ schema:Organization"]:::org
    RoleInActivity["RoleInActivity </br> rdip:RoleInActivity </br> ⊑ prov:Role"]:::role
    ActivityAssociation["ActivityAssociation </br> rdip:ActivityAssociation </br> ⊑ prov:Association"]:::role

    %% ── SOFTWARE ──
    SoftwareApplication["SoftwareApplication </br> rdip:SoftwareApplication </br> ≡ schema:SoftwareApplication | ⊑ prov:Entity"]:::software
    SoftwareDependency["SoftwareDependency </br> rdip:SoftwareDependency </br> ⊑ prov:Entity"]:::software
    ComputingEnvironment["ComputingEnvironment </br> rdip:ComputingEnvironment </br> ⊑ prov:Entity, schema:Thing"]:::env
    EnvironmentSpec["EnvironmentSpec </br> rdip:EnvironmentSpec </br> ⊑ prov:Entity"]:::env

    %% ── PARAMETERS ──
    Parameter["Parameter </br> rdip:Parameter </br> ⊑ prov:Entity, schema:PropertyValue"]:::param
    RandomSeed["RandomSeed </br> rdip:RandomSeed </br> ⊑ rdip:Parameter"]:::param
    Method["Method </br> rdip:Method </br> ⊑ prov:Plan, schema:CreativeWork"]:::method

    %% ── DATASETS ──
    Dataset["Dataset </br> dcat:Dataset </br> ≡ schema:Dataset"]:::dataset
    EvaluationResult["EvaluationResult </br> rdip:EvaluationResult </br> ⊑ prov:Entity, schema:Observation"]:::result

    %% ── EXECUTION RECIPES (v2.1) ──
    ExecutionRecipe["ExecutionRecipe </br> rdip:ExecutionRecipe </br> ⊑ prov:Plan"]:::recipe
    SetupStep["SetupStep </br> rdip:SetupStep </br> ⊑ prov:Plan"]:::recipe

    %% ── PUBLICATIONS ──
    Article["Article / Document </br> bibo:Article / bibo:Document </br> ⊑ schema:ScholarlyArticle"]:::article

    %% ── PROJECT RELATIONS ──
    ResearchProject -- hasActivity --> ResearchActivity
    ResearchProject -- hasParticipant --> Person
    ResearchProject -- hasLeadOrganization --> Organization
    ResearchProject -- hasOutput --> Dataset
    ResearchProject -- hasOutput --> SoftwareApplication
    ResearchProject -- hasOutput --> Article

    %% ── ACTIVITY RELATIONS ──
    ResearchActivity -- isPartOfProject --> ResearchProject
    ResearchActivity -- follows / precedes --> ResearchActivity
    ResearchActivity -- usedDataset --> Dataset
    ResearchActivity -- generatesDataset --> Dataset
    ResearchActivity -- usedSoftware --> SoftwareApplication
    ResearchActivity -- usedMethod --> Method
    ResearchActivity -- executedIn --> ComputingEnvironment
    ResearchActivity -- hasParameter --> Parameter
    ResearchActivity -- hasActivityRole --> RoleInActivity
    ResearchActivity -- prov:qualifiedAssociation --> ActivityAssociation

    %% ── SPECIALIZED ACTIVITY RELATIONS ──
    SoftwareDevelopmentActivity -- generatesSoftware --> SoftwareApplication
    DataAnalysisActivity -- generatesResult --> EvaluationResult
    PublicationActivity -- generatesPublication --> Article

    %% ── ROLE RELATIONS ──
    RoleInActivity -- rolePerformedBy --> Person
    ActivityAssociation -- prov:agent --> Person
    ActivityAssociation -- prov:hadRole --> RoleInActivity

    %% ── SOFTWARE RELATIONS ──
    SoftwareApplication -- softwareDependency --> SoftwareDependency
    SoftwareApplication -- isOutputOf --> ResearchProject
    ComputingEnvironment -- hasEnvironmentSpec --> EnvironmentSpec

    %% ── DATASET RELATIONS ──
    Dataset -- derivedFrom --> Dataset
    Dataset -- wasGeneratedBy --> ResearchActivity
    Dataset -- isOutputOf --> ResearchProject

    %% ── PARAMETER HIERARCHY ──
    Parameter -- subClassOf --> RandomSeed

    %% ── PUBLICATION RELATIONS ──
    Article -- citesDataset --> Dataset
    Article -- isOutputOf --> ResearchProject

    %% ── EXECUTION RECIPE RELATIONS (v2.1) ──
    ResearchActivity -- hasExecutionRecipe --> ExecutionRecipe
    ExecutionRecipe -- setupStep --> SetupStep
    ExecutionRecipe -- requiresDataset --> Dataset
    ExecutionRecipe -- producesMetric --> EvaluationResult
```

## v2.1 — Execution Recipes

`rdip:ExecutionRecipe` makes the procedure for reproducing a reported result an
explicit, machine-readable object rather than prose in a README. It is a
`prov:Plan`: the plan an activity follows, not the activity itself.

| Term | Kind | Notes |
|---|---|---|
| `rdip:ExecutionRecipe` | class ⊑ `prov:Plan` | the recipe as a whole |
| `rdip:SetupStep` | class ⊑ `prov:Plan` | one ordered preparatory action |
| `rdip:hasExecutionRecipe` | object property | activity → recipe; shortcut for `prov:qualifiedAssociation`/`prov:hadPlan` |
| `rdip:setupStep` | object property | recipe → step |
| `rdip:requiresDataset` | object property | recipe → `dcat:Dataset` |
| `rdip:producesMetric` | object property | recipe → `rdip:EvaluationResult` |
| `rdip:runCommand` | data property | the command, verbatim |
| `rdip:entryPoint` | data property | script the command invokes |
| `rdip:stepOrder` | data property | 1-based position of a setup step |
| `rdip:stepCommand` | data property | the step's shell command |
| `rdip:requiresCheckpoint` | data property | pretrained weights, path or URL |
| `rdip:recipeConfidence` | data property | `high` or `low`, self-reported by the extractor |

Three modelling choices are deliberate and worth stating:

**Setup steps are a class, not repeated literals.** RDF imposes no order on
repeated properties, and setup order is load-bearing — a download must precede
the extraction that consumes it. `rdip:stepOrder` carries the sequence.

**`requiresDataset` points at a `dcat:Dataset`, not a name.** A requirement that
resolves to a distribution and an access level makes a real blocker visible: a
dataset released only on application defeats reproduction even when the command
is perfect.

**`producesMetric` reuses `rdip:EvaluationResult`** from Section 5 rather than
introducing new metric vocabulary, so comparing a re-run against the paper's
claim is a comparison of two `EvaluationResult` instances.

A recipe whose `rdip:runCommand` still contains an unfilled placeholder should be
recorded verbatim with a low `rdip:recipeConfidence`, never repaired by guessing
a value: a fabricated path converts a detectable documentation gap into a silent
wrong answer. See `core/examples.ttl`, case study 4, for a real extracted recipe.
