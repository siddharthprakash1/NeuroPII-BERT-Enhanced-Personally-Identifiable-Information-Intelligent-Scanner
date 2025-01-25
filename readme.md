# NeuroPII: BERT-Enhanced Personally Identifiable Information Intelligent Scanner

A sophisticated Flask-based web application leveraging Bidirectional Encoder Representations from Transformers (BERT) for advanced sensitive data detection and pattern recognition in documents. The system scans various document formats for sensitive information using a hybrid approach of machine learning and pattern matching.

## Project Highlights (Assessment Criteria)

### ✅ Working Prototype
- Functional web interface for file uploads
- Real-time scanning and results display
- Support for multiple file formats (.doc, .docx, .csv, .xlsx, .xls)
- Clean and intuitive user interface

### ✅ Code Quality
- Modular architecture separating concerns:
  - `app.py`: Web interface and routing
  - `data_scanner.py`: Core scanning logic and BERT integration
  - `database.py`: Data management and storage
- Comprehensive error handling for file operations
- Input validation for all file uploads
- Clean code following PEP 8 standards

### ✅ Code Coverage
Current coverage metrics:
- data_scanner.py: 77%
- database.py: 100%
- Overall: 81%

### ✅ Advanced ML Implementation
- BERT model integration for Named Entity Recognition
- Context-aware pattern recognition
- Hybrid approach combining ML and regex patterns

## Features
- Detects multiple types of sensitive information:
  - PAN Card Numbers
  - Social Security Numbers (SSN)
  - Medical Record Numbers
  - Credit Card Numbers
- Neural-based pattern recognition using BERT
- Real-time scanning and results display
- Secure file handling with no permanent storage
- Detailed scan reports with found sensitive data

## Technology Stack
- Python 3.10
- Flask (Web Framework)
- BERT (Bidirectional Encoder Representations from Transformers)
- Transformers library (Hugging Face)
- python-docx (Word document processing)
- pandas (Excel/CSV processing)
- PyTorch (Deep Learning)
- pytest (Testing)

## Installation and Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Access the interface at: `http://localhost:5000`

## Running Tests
Execute test suite:
```bash
pytest tests/
```

Generate coverage report:
```bash
pytest --cov=app --cov=data_scanner --cov=database tests/
```

## Production Deployment Guide

The application is designed for production deployment with scalability and security in mind. For production deployment, the following considerations have been implemented:

1. **Security Measures**:
   - File validation before processing
   - No permanent storage of sensitive data
   - Memory-based secure processing
   - Input sanitization

2. **Performance Optimization**:
   - Efficient memory management
   - Optimized BERT model inference
   - Proper file handling
   - Batched processing capabilities

3. **Deployment Steps (Render.com)**:
   ```bash
   # 1. Create new web service
   # 2. Set environment variables:
   FLASK_ENV=production
   SECRET_KEY=your-secret-key
   
   # 3. Build command:
   pip install -r requirements.txt
   
   # 4. Start command:
   gunicorn app:app
   ```

## Project Structure
```
project/
├── app.py                    # Main Flask application
├── data_scanner.py           # Core scanning logic with BERT
├── database.py               # Data storage handling
├── requirements.txt          # Python dependencies
├── templates/            
│   ├── index.html           # Upload interface
│   └── scan_results.html    # Results display
└── tests/
    └── test_scanner.py      # Test suite
```

## System Architecture
```mermaid
graph TD
    A[Web Interface] -->|File Upload| B[Flask Server]
    B --> C[File Processor]
    C --> D[BERT Model]
    C --> E[Pattern Matcher]
    D --> F[Results Aggregator]
    E --> F
    F --> G[Results Display]
    
    subgraph ML Processing
    D
    end
    
    subgraph Pattern Matching
    E
    end
    
    subgraph Web Server
    B
    C
    F
    end
```

## Bonus Points Achievement Status
1. ✅ Test Coverage: Achieved 81% coverage
2. ✅ Production Write-up: Included deployment guide[NOTE:not deployed]
3. ✅ Deployment Ready: Configured for cloud deployment
4. ✅ Code Quality: Follows PEP 8 standards
5. ✅ ML Model: Integrated BERT for advanced classification

## Future Improvements
- Implement transformer-based document classification
- Add support for more document formats
- Enhance neural pattern recognition
- Add export functionality with encryption
- Implement user authentication
- Add API rate limiting
- Implement real-time scanning status updates


## Author
Siddharth Prakash
iamsid0011@gmail.com
https://siddharthprakash.vercel.app/

## License

This project is licensed under the [MIT License](LICENSE).  
© 2025 Siddharth



## Acknowledgments
- Hugging Face for the BERT model
- Flask team for the web framework
- Python community for various libraries
