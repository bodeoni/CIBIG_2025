````mermaid
mindmap
  root((Determine Pathogen Responsible))
    Context & Epidemiology
      Host: Sweet potato
      Location: Kénédougou
      Symptoms
        Mosaic & Yellowing
        Deformation & Growth reduction
      Risk Factors
        Mixed cropping Tomato/Pepper/Okra
        Emerging recombinant pathogens
    Wet Lab Input
      Sampling
        Symptomatic leaves
      Library Prep
        DNA Extraction
        RCA: TempliPhi Polymerase
        Enrichment: Circular DNA
        Barcoding: Native Barcoding 96
      Sequencing
        Platform: MinION Mk1C
        Flowcell: SpotON
    Bioinformatics Pipeline
      QC & Demux
        NanoPlot
        Guppy/Dorado
        Check: Long reads expected
      Preprocessing
        Trimming: Porechop
        Filtering: Chopper
        Host Removal
          Tool: Minimap2
          Ref: Ipomoea batatas
      Taxonomic Classification
        Read-based: Kraken2
        Protein-based: Kaiju
      Assembly Strategy
        De Novo: Flye --meta
        Correction: Canu
        Polishing: Medaka
    Pathogen Characterization
      Identification
        BLASTn / BLASTx
        CheckV: Confirm Circularity
      Mixed Infections
        Map reads to assembly
        Detect coverage variation
      Recombination Analysis
        Tool: RDP5
        Detect: Breakpoints
      Phylogenetics
        Alignment: MAFFT
        Tree: IQ-TREE 2
    Reporting & Decisions
      Identify Pathogen Diversity
      Assess Risk
        Endemic vs Emerging
        Recombinant lineages
      Output
        Decision-oriented report
        Surveillance support
