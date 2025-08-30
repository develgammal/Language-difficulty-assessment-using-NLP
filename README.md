# Multilingual Language Learning Tool

## 📚 Project Overview

This project implements a comprehensive language learning tool that analyzes subtitle files (.srt) and provides word difficulty assessments using three distinct computational methodologies. The tool combines natural language processing, machine learning, and data visualization to create an academic experiment comparing different approaches to word difficulty classification.

**✨ NEW: Enhanced with comprehensive caching system for production-ready performance!**

## 🎯 Objectives

1. **Topic-based Sentence Grouping**: Automatically group sentences from subtitle files by semantic topics using BERTopic
2. **Triple Word Difficulty Analysis**: Compare three methods for determining word difficulty:
   - **Method A: Word Frequency** - Traditional approach based on corpus frequency
   - **Method B: Embedding L2 Norm** - Experimental approach using embedding magnitudes
   - **Method C: ML Model** - Supervised learning approach with engineered features
3. **Comparative Visualization**: Side-by-side color-coded comparison of all three methods
4. **Production-Ready Caching**: Intelligent caching system for instant subsequent runs

## ⚡ Performance Features

- **First Run**: Full corpus processing and model training (~10-20 minutes)
- **Subsequent Runs**: Instant loading from cache (< 30 seconds)
- **Language-Specific Caching**: Separate optimized caches for each language
- **Configurable Processing**: No default limits, with optional debugging limits
- **Force Rebuild Options**: Selective regeneration of cached components

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment support (venv)

### Installation

1. **Clone or download this project to your local machine**

2. **Navigate to the project directory:**
   ```bash
   cd NLP_UNI_Projekt
   ```

3. **Create and activate the virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv nlp_env

   # Activate on Windows (Git Bash)
   source nlp_env/Scripts/activate

   # Activate on macOS/Linux
   source nlp_env/bin/activate
   ```

4. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook multilingual_language_learning_tool.ipynb
   ```

## 📁 Project Structure

```
NLP_UNI_Projekt/
├── multilingual_language_learning_tool.ipynb  # Main notebook
├── ENGLISH_CERF_WORDS.csv                     # CEFR word classifications
├── sample_subtitles.srt                       # Sample subtitle file
├── requirements.txt                           # Python dependencies
├── nlp_env/                                   # Virtual environment
└── README.md                                  # This file
```

## 🔧 Configuration

The notebook includes a central configuration cell where you can customize:

- **Target Language**: Set using ISO 639-1 codes ('es', 'pt', 'fr', 'de', etc.)
- **Subtitle File Path**: Point to your own .srt file
- **Model Selection**: Choose different multilingual models
- **Difficulty Tiers**: Adjust CEFR level boundaries
- **Color Scheme**: Customize visualization colors

## 📊 Features

### Method A: Word Frequency Analysis
- Downloads large corpora using OPUS Books dataset
- Calculates word frequencies across multiple texts
- Maps frequency ranks to CEFR difficulty levels
- Proven approach based on linguistic research

### Method B: Embedding Norm Analysis
- Uses sentence transformer models for multilingual embeddings
- Calculates L2 norms of word embedding vectors
- Novel approach hypothesizing correlation between norm and difficulty
- Handles subword tokenization challenges

### Topic Modeling
- Implements BERTopic for semantic clustering
- Groups sentences by thematic similarity
- Provides context-aware difficulty analysis
- Supports multilingual content

### Visualization & Analysis
- Color-coded sentence display for both methods
- Side-by-side comparison interface
- Quantitative correlation analysis
- Interactive topic exploration

## 🎨 Color Coding System

- 🟢 **A1 (Green)**: Beginner level words
- 🔵 **A2 (Light Green)**: Elementary level words
- 🟡 **B1 (Amber)**: Intermediate level words
- 🟠 **B2 (Orange)**: Upper intermediate level words
- 🔴 **C1 (Red)**: Advanced level words
- 🟤 **C2 (Dark Red)**: Proficiency level words
- ⚫ **OOV (Grey)**: Out of vocabulary words

## 📈 Analysis Capabilities

### Quantitative Metrics
- Agreement rate between methods
- Correlation coefficients
- Confusion matrices
- Distribution analysis

### Qualitative Insights
- Visual comparison of classification approaches
- Topic-specific difficulty patterns
- Method-specific strengths and weaknesses
- Domain-specific performance analysis

## 🔬 Research Applications

This tool can be used for:
- **Linguistic Research**: Comparing computational difficulty metrics
- **Educational Technology**: Developing adaptive learning systems
- **Content Assessment**: Evaluating text difficulty for language learners
- **Curriculum Design**: Creating level-appropriate learning materials

## 🛠️ Customization

### Adding New Languages
1. Update `TARGET_LANGUAGE` in the configuration cell
2. Ensure OPUS Books dataset supports your language
3. Consider language-specific preprocessing needs

### Using Your Own Subtitle Files
1. Place your .srt file in the project directory
2. Update `SRT_FILE_PATH` in the configuration
3. Run the notebook with your custom content

### Modifying Difficulty Tiers
1. Adjust `FREQUENCY_TIERS` for different rank ranges
2. Modify `NORM_TIERS` for different percentile cutoffs
3. Customize `COLOR_MAP` for your preferred visualization

## 🤝 Contributing

This project welcomes contributions in the form of:
- Additional language support
- Alternative difficulty calculation methods
- Enhanced visualization techniques
- Performance optimizations
- Documentation improvements

## 📚 Dependencies

Key libraries used:
- **BERTopic**: Topic modeling and clustering
- **Sentence Transformers**: Multilingual embeddings
- **Datasets**: Access to linguistic corpora
- **NLTK**: Natural language processing tools
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Data visualization
- **PySRT**: Subtitle file parsing

## ⚠️ Notes

- First run may take time due to model downloads
- Internet connection required for dataset access
- Memory usage depends on corpus size and model selection
- Some features may require GPU for optimal performance

## 📄 License

This project is intended for educational and research purposes. Please respect the licenses of the underlying datasets and models used.

## 🆘 Troubleshooting

### Common Issues:
1. **Model Download Failures**: Ensure stable internet connection
2. **Memory Errors**: Reduce corpus size in configuration
3. **NLTK Data Missing**: Run nltk download commands in notebook
4. **Virtual Environment Issues**: Recreate environment if packages conflict

### Support:
For technical issues, refer to the notebook's inline documentation and error handling mechanisms.

---

*This tool represents a novel approach to computational linguistics in language learning, bridging traditional frequency-based methods with modern embedding-based techniques.*


............

language specific hard coded logic or regex or vars that are not in the central config?

update introduction and outro markdowns to refelct the current number of methods we are implementing?

..............

ask ai to judge best approaches now linguistically compared to estimation of Actual difficulty of hte words since it is an llm you cna feed it the dataset itself as well

some meta analysis or model that kind of averages eveything out?

..........
final commentary and include also checking that intro and outro make sense, you can also create custom sample subtitles or some sort of test with known preassumtion then comparing it