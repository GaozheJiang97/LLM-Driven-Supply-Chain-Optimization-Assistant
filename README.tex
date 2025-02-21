\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{float}
\usepackage{subcaption}
\usepackage{caption}
\geometry{margin=1in}

\title{LLM-Driven Supply Chain Optimization Assistant: Project Report}
\author{Gaozhe Jiang}
\date{\today}

\begin{document}

\maketitle

\tableofcontents
\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Project Title and Team Members}
\begin{itemize}
    \item \textbf{Project Title:} LLM-Driven Supply Chain Optimization Assistant
    \item \textbf{Team Member:}
    \begin{itemize}
        \item Gaozhe Jiang (e0945601@u.nus.edu)
    \end{itemize}
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Problem Statement}
Efficient supply chain management is a critical driver for operational success in modern businesses. Even minor inefficiencies in planning, resource allocation, and logistics can lead to significant cost overruns, delivery delays, and overall operational disruptions. Many companies struggle to formulate and solve the complex optimization problems required to streamline these processes, especially when decision-makers lack deep expertise in operations research (OR).

\textbf{The Challenge:}  
Develop an intelligent system that allows users to describe their supply chain problems in plain, natural language. The system automatically extracts key parameters and formulates a corresponding optimization model to compute an optimal shipment plan. By bridging the gap between natural language and mathematical optimization, the system aims to democratize advanced analytical methods.

\textbf{Importance:}
\begin{itemize}
    \item \textbf{Accessibility:} Enables business managers and analysts to leverage advanced OR without needing extensive technical training.
    \item \textbf{Efficiency:} Automates the translation from natural language descriptions to mathematical models, saving time and reducing errors.
    \item \textbf{Cost Savings:} Optimizes resource allocation to minimize shipping and transportation costs.
    \item \textbf{Scalability:} Establishes a scalable foundation for tackling more complex supply chain challenges in the future.
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Solution Approach}
Our solution integrates modern Large Language Model (LLM) techniques with classical optimization methods using a modular, agent-based architecture.

\subsection*{Key Components:}
\begin{enumerate}[label=\arabic*.]
    \item \textbf{Natural Language Parsing with LLMs:}
    \begin{itemize}
        \item We simulate an LLM parser that converts natural language descriptions into structured data by extracting key parameters such as warehouse names, store names, available supply, demand requirements, and shipping costs.
        \item \emph{Future Enhancement:} Upgrade this module using frameworks like \texttt{LangChain} or \texttt{DSPy} and live API calls (e.g., OpenAI’s GPT-4) to dynamically process user inputs.
    \end{itemize}
    \item \textbf{Optimization Module:}
    \begin{itemize}
        \item The extracted parameters are used to formulate a transportation problem as a linear programming (LP) model.
        \item We utilize \texttt{PuLP}, a Python library for LP, to construct and solve the optimization model. The objective is to minimize the total shipping cost while satisfying supply and demand constraints.
    \end{itemize}
    \item \textbf{Interactive Web Interface:}
    \begin{itemize}
        \item A \texttt{Streamlit} web application serves as the user interface, allowing users to input a natural language description of their supply chain problem and view the parsed parameters and optimization results in a clear, interactive format.
    \end{itemize}
\end{enumerate}

\subsection*{System Architecture Overview:}
\begin{center}
\begin{verbatim}
       +----------------------------+
       | User Input (Natural      |
       | Language Description)    |
       +-------------+--------------+
                     |
                     v
       +-----------------------------+
       | LLM Parser (Simulated or    |
       | Live via LangChain/OpenAI)  |
       +-------------+---------------+
                     |
                     v
       +---------------------------------------+
       | Data Extraction & Parameter Formation |
       | (Warehouses, Stores, Supply, Demand,   |
       | Shipping Costs)                        |
       +----------------+------------------------+
                     |
                     v
       +--------------------------------------+
       | Optimization Module (PuLP)           |
       | (Formulate \& Solve Transportation LP)|
       +----------------+-----------------------+
                     |
                     v
       +-----------------------------+
       | Streamlit Web Interface     |
       | (Display Results \&         |
       | Explanation)                |
       +-----------------------------+
\end{verbatim}
\textbf{Figure 1: System Architecture Diagram}
\end{center}

*Note: The current prototype uses fixed example data to simulate LLM output. Future iterations will incorporate live LLM parsing.*

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Instructions: How to Run the Code}
\subsection*{Prerequisites}
\begin{itemize}
    \item \textbf{Python 3.8+} is required. Verify your version by running:
    \begin{verbatim}
python --version
    \end{verbatim}
    \item (Optional) \textbf{OpenAI API Key:} If you plan to integrate a live LLM for parsing, obtain an API key from OpenAI and set it as an environment variable (\texttt{OPENAI_API_KEY}).
\end{itemize}

\subsection*{Environment Setup}
\begin{enumerate}[label=\arabic*.]
    \item \textbf{Clone the Repository:}
    \begin{verbatim}
git clone https://github.com/yourusername/LLM-SupplyChain-Optimization.git
cd LLM-SupplyChain-Optimization
    \end{verbatim}
    \item \textbf{Create and Activate a Virtual Environment:}
    \begin{verbatim}
python -m venv venv
    \end{verbatim}
    On macOS/Linux:
    \begin{verbatim}
source venv/bin/activate
    \end{verbatim}
    On Windows:
    \begin{verbatim}
venv\Scripts\activate
    \end{verbatim}
    \item \textbf{Install Dependencies:}  
    The dependencies are listed in \texttt{requirements.txt}. Install them using:
    \begin{verbatim}
pip install -r requirements.txt
    \end{verbatim}
\end{enumerate}

\subsection*{Configuration}
\begin{itemize}
    \item (Optional) Set your OpenAI API key if you plan to use live LLM parsing:
    \begin{verbatim}
# On macOS/Linux:
export OPENAI_API_KEY=your_openai_api_key

# On Windows:
set OPENAI_API_KEY=your_openai_api_key
    \end{verbatim}
\end{itemize}

\subsection*{Running the Application}
\begin{enumerate}[label=\arabic*.]
    \item \textbf{Start the Streamlit Application:}
    \begin{verbatim}
streamlit run app.py
    \end{verbatim}
    \item \textbf{Using the Application:}
    \begin{itemize}
        \item A browser window will open displaying the application interface.
        \item Enter a natural language description of your supply chain problem into the text area.
        \item \textbf{Example Input:}
        \begin{verbatim}
"We have 2 warehouses (A and B) and 3 stores (X, Y, Z). Warehouse A has 100 units,
 Warehouse B has 80 units. Store X requires 50 units, Store Y requires 70 units, and 
 Store Z requires 40 units. Shipping costs per unit are as follows: A to X: 2, A to Y: 4,
 A to Z: 5, B to X: 3, B to Y: 1, B to Z: 2. Please minimize the total shipping cost."
        \end{verbatim}
        \item Click the \textbf{Optimize} button.
        \item The application will display:
        \begin{itemize}
            \item The parsed parameters (warehouses, stores, supply, demand, shipping costs).
            \item An explanation of the parsing process.
            \item The optimized shipment plan along with the total shipping cost.
        \end{itemize}
    \end{itemize}
\end{enumerate}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Results}
The current prototype demonstrates several key capabilities:

\subsection*{Natural Language Parsing (Simulated)}
\begin{itemize}
    \item The system simulates an LLM-based parser that extracts essential supply chain details from a natural language input.
    \item Although the current implementation uses fixed example data, it reflects the expected structure for a real-world scenario.
\end{itemize}

\subsection*{Optimization of the Transportation Problem}
\begin{itemize}
    \item Using \texttt{PuLP}, the system formulates a linear programming model that minimizes the total shipping cost while ensuring:
    \begin{itemize}
        \item Shipments from each warehouse do not exceed available inventory.
        \item Each store receives at least its required quantity.
    \end{itemize}
\end{itemize}

\subsection*{Interactive User Interface}
\begin{itemize}
    \item The \texttt{Streamlit} web app offers an intuitive interface for inputting the supply chain problem description and viewing the optimization results.
    \item Users can immediately see the parsed data and a detailed shipment plan.
\end{itemize}

\subsection*{Sample Optimization Results}
\textbf{Optimization Results (Example):} \\
\textbf{Status:} Optimal \\
\textbf{Total Shipping Cost:} 340.0 \\
\textbf{Shipment Plan:}
\begin{itemize}
    \item From Warehouse A to Store X: 50.0 units
    \item From Warehouse A to Store Y: 30.0 units
    \item From Warehouse A to Store Z: 0.0 units
    \item From Warehouse B to Store X: 0.0 units
    \item From Warehouse B to Store Y: 40.0 units
    \item From Warehouse B to Store Z: 40.0 units
\end{itemize}

\subsection*{Figures}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{results_plot.png}
    \caption{Sample Plot of Optimized Shipment Quantities}
    \label{fig:results_plot}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{ui_screenshot.png}
    \caption{Screenshot of the Streamlit User Interface}
    \label{fig:ui_screenshot}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Future Work}
To extend and improve the system beyond the hackathon, our planned enhancements include:
\begin{enumerate}[label=\arabic*.]
    \item \textbf{Integrate Live LLM Parsing:}  
    Replace the simulated parser with a live integration using \texttt{LangChain} and the OpenAI API to dynamically extract parameters from natural language inputs.
    
    \item \textbf{Enhance the Optimization Model:}  
    Extend the current transportation model to handle more complex scenarios such as multi-modal transportation, dynamic inventory management, and incorporating uncertainty in supply/demand.
    
    \item \textbf{Improve the User Interface:}  
    Upgrade the \texttt{Streamlit} app with interactive visualizations (e.g., dynamic charts, graphs), detailed explanations of the optimization process, and robust error handling.
    
    \item \textbf{Incorporate External Data Sources:}  
    Connect the system to real-time data APIs or databases to automatically update model parameters and improve decision accuracy.
    
    \item \textbf{Advanced Agentic Orchestration:}  
    Explore additional frameworks such as \texttt{LangGraph} and \texttt{DSPy} to manage multi-agent interactions and orchestrate more sophisticated workflows.
\end{enumerate}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Code Organization}
The repository is organized as follows:
\begin{verbatim}
LLM-SupplyChain-Optimization/
├── README.tex         % This comprehensive LaTeX project report
├── requirements.txt   % List of Python dependencies
└── app.py             % Main application code (Streamlit web app)
\end{verbatim}
Each section of the code is well-commented and organized for clarity and ease of maintenance.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{License}
This project is licensed under the MIT License. See the LICENSE file for details.

\end{document}
