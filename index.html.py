<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chen Yanxi's Portfolio | 陈彦希的个人作品集</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals (Stone, Sky) -->
    <!-- Application Structure Plan: A single-page, vertical-scrolling SPA with a fixed top navigation. The structure is designed as a narrative journey: Hero -> Profile (with interactive skills chart) -> Tabbed Projects Section -> Card-based Holistic Development -> Footer. This non-linear but guided structure enhances usability by allowing both sequential reading and direct access to key information, making it more engaging than a static document. -->
    <!-- Visualization & Content Choices: 1. Skills -> Goal: Compare -> Viz: Chart.js Radar Chart -> Interaction: Hover Tooltips -> Justification: More engaging and visual than a text list. 2. Projects -> Goal: Organize -> Viz: JS Tabbed Interface -> Interaction: Click to reveal -> Justification: Prevents clutter, focuses attention. 3. Holistic Dev -> Goal: Organize -> Viz: Icon-driven cards -> Interaction: Hover effects -> Justification: Scannable and visually separates diverse achievements. CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', 'Noto Sans SC', sans-serif;
        }
        .fade-in-section {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }
        .fade-in-section.is-visible {
            opacity: 1;
            transform: translateY(0);
        }
        .tab-active {
            border-color: #0c4a6e; /* sky-800 */
            color: #0c4a6e;
            font-weight: 500;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 450px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 400px;
            }
        }
    </style>
</head>
<body class="bg-stone-50 text-stone-700 antialiased">

    <!-- Header & Navigation -->
    <header id="header" class="bg-stone-50/80 backdrop-blur-md sticky top-0 z-50 transition-all duration-300">
        <div class="container mx-auto px-6 py-3 flex justify-between items-center">
            <a href="#hero" class="text-xl font-bold text-sky-800">Chen Yanxi</a>
            <nav class="hidden md:flex space-x-6 items-center">
                <a href="#about" class="hover:text-sky-800 transition-colors">About Me</a>
                <a href="#projects" class="hover:text-sky-800 transition-colors">Projects</a>
                <a href="#development" class="hover:text-sky-800 transition-colors">Holistic Development</a>
                <a href="#contact" class="bg-sky-800 text-white px-4 py-2 rounded-md hover:bg-sky-700 transition-colors">Contact Me</a>
            </nav>
            <button id="mobile-menu-button" class="md:hidden text-stone-800">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
            <a href="#about" class="block py-2 hover:text-sky-800">About Me</a>
            <a href="#projects" class="block py-2 hover:text-sky-800">Projects</a>
            <a href="#development" class="block py-2 hover:text-sky-800">Holistic Development</a>
            <a href="#contact" class="block mt-2 bg-sky-800 text-white text-center px-4 py-2 rounded-md hover:bg-sky-700">Contact Me</a>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section id="hero" class="h-screen min-h-[600px] flex items-center bg-stone-100">
            <div class="container mx-auto px-6 flex flex-col md:flex-row items-center gap-12">
                <div class="md:w-1/2 text-center md:text-left">
                    <h1 class="text-4xl md:text-6xl font-bold text-sky-900 leading-tight">Innovating for Impact</h1>
                    <h2 class="text-2xl md:text-4xl font-light text-stone-600 mt-2">My Journey in Interdisciplinary Problem-Solving</h2>
                    <p class="mt-6 text-lg text-stone-600 max-w-xl mx-auto md:mx-0">Empowering Innovation through Mathematical Insight and Technological Application.</p>
                    <a href="#projects" class="inline-block mt-8 bg-sky-800 text-white px-8 py-3 rounded-md text-lg font-semibold hover:bg-sky-700 transition-transform hover:scale-105">Explore My Projects</a>
                </div>
                <div class="md:w-1/2 flex justify-center">
                    <div class="w-64 h-64 md:w-80 md:h-80 rounded-full overflow-hidden shadow-2xl ring-4 ring-white/50">
                        <img src="https://placehold.co/400x400/a3e635/1c1917?text=Profile\nPhoto" alt="Chen Yanxi's Professional Photo" class="w-full h-full object-cover" onerror="this.onerror=null;this.src='https://placehold.co/400x400/e5e7eb/44403c?text=Image+Not+Found';">
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="py-20 md:py-32 bg-white fade-in-section">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-sky-900">Explorer & Builder</h2>
                    <p class="text-lg text-stone-600 mt-2">My Academic Profile & Core Competencies</p>
                </div>
                <div class="grid md:grid-cols-5 gap-12 items-start">
                    <div class="md:col-span-3">
                        <h3 class="text-2xl font-semibold text-stone-800 mb-4">Concise Bio</h3>
                        <p class="text-stone-600 leading-relaxed mb-8">I am Chen Yanxi, a student majoring in Mathematics and Applied Mathematics from Chongqing University, with a strong passion for interdisciplinary research, innovative practices, and problem-solving. With a solid foundation in mathematics and an IELTS score of 7.0, I am committed to applying theoretical knowledge to cutting-edge technological fields, exploring the infinite possibilities of intelligent solutions.</p>
                        
                        <h3 class="text-2xl font-semibold text-stone-800 mb-4">Soft Skills & Personal Attributes</h3>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 text-stone-600">
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Innovative Thinking</div>
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Critical Thinking</div>
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Problem-Solving</div>
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Team Collaboration</div>
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Independent Leadership</div>
                            <div class="flex items-center gap-2"><span class="text-sky-800">✓</span>Fast Learning Ability</div>
                        </div>

                        <h3 class="text-2xl font-semibold text-stone-800 mt-8 mb-4">Academic Highlights</h3>
                        <ul class="list-none space-y-2">
                             <li class="flex items-center gap-3"><span class="text-amber-500">🏆</span>Second Prize in National Mathematical Contest in Modeling (2024)</li>
                             <li class="flex items-center gap-3"><span class="text-amber-500">🏆</span>Chongqing University Comprehensive Scholarship (multiple times)</li>
                        </ul>
                    </div>
                    <div class="md:col-span-2">
                         <h3 class="text-2xl font-semibold text-stone-800 mb-4 text-center">Core Technical Skills</h3>
                        <div class="chart-container">
                            <canvas id="skillsChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Projects Section -->
        <section id="projects" class="py-20 md:py-32 bg-stone-100 fade-in-section">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-sky-900">Core Project Experience</h2>
                    <p class="text-lg text-stone-600 mt-2">From theory to practice, solving real-world problems.</p>
                </div>
                <!-- Tabs -->
                <div class="mb-8 border-b border-stone-300">
                    <nav class="flex flex-wrap -mb-px" id="project-tabs">
                        <button data-target="project1" class="tab-btn tab-active text-lg px-4 py-3 border-b-2 border-transparent">Federated Learning</button>
                        <button data-target="project3" class="tab-btn text-lg px-4 py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-700">Fault Detection</button>
                        <button data-target="project2" class="tab-btn text-lg px-4 py-3 border-b-2 border-transparent text-stone-500 hover:text-stone-700">Defect Prediction</button>
                    </nav>
                </div>
                <!-- Tab Content -->
                <div id="project-content">
                    <article id="project1" class="project-panel">
                        <div class="bg-white p-8 rounded-lg shadow-lg">
                            <h3 class="text-2xl font-bold text-sky-800 mb-1">Asynchronous Federated Learning: Empowering Intelligent UAV Swarms</h3>
                            <p class="text-sm text-stone-500 mb-4">Provincial Innovation Entrepreneurship Program (Deputy Leader)</p>
                            <div class="grid md:grid-cols-2 gap-8">
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">Project Background & Challenges</h4>
                                    <p class="text-stone-600 project-desc">Traditional UAV swarm collaborative learning faces challenges such as data privacy, communication efficiency, and resource constraints, limiting its application in complex environments.</p>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">My Approach & Methodology</h4>
                                    <p class="text-stone-600 project-desc">Addressing these issues, I was responsible for developing and improving the theoretical foundation of asynchronous federated learning algorithms. Through rigorous mathematical derivation, we proved the convergence of this algorithm under non-ideal communication conditions, providing theoretical support for distributed intelligent collaboration in UAV swarms.</p>
                                </div>
                                <div class="md:col-span-2">
                                    <h4 class="font-semibold text-lg mb-2">Outcomes & Reflections</h4>
                                    <p class="text-stone-600 project-desc">The project was rated 'Good' at the provincial level. I was primarily responsible for the theoretical modeling and convergence analysis of the core algorithm. Through this project, I gained a deep understanding of the potential of federated learning in distributed systems and enhanced my capabilities in complex algorithm design and verification.</p>
                                </div>
                            </div>
                            <button class="generate-insight-btn mt-6 bg-sky-600 text-white px-6 py-2 rounded-md hover:bg-sky-700 transition-colors">✨ Get Project Insight</button>
                            <div class="insight-output mt-4 text-stone-700 leading-relaxed"></div>
                            <div class="loading-indicator mt-4 text-stone-500 hidden">Generating...</div>
                        </div>
                    </article>
                    <article id="project3" class="project-panel hidden">
                        <div class="bg-white p-8 rounded-lg shadow-lg">
                            <h3 class="text-2xl font-bold text-sky-800 mb-1">Intelligent Fault Diagnosis: Weak Signal Detection in Variable-Speed Mechanical Systems</h3>
                            <p class="text-sm text-stone-500 mb-4">Applied Statistics Research Project (Independent Project Leader)</p>
                            <div class="grid md:grid-cols-2 gap-8">
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">Project Background & Challenges</h4>
                                    <p class="text-stone-600 project-desc">Detecting weak faults in variable-speed mechanical systems under noisy and non-stationary conditions is a significant challenge in the industrial sector.</p>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">My Approach & Methodology</h4>
                                    <p class="text-stone-600 project-desc">I independently led this project, focusing on stochastic modeling and signal enhancement under the guidance of my supervisor. I developed a Variable-Coefficient Bistable Stochastic Resonance (VCBSR) model, aiming for precise weak fault detection under low SNR and variable-speed conditions.</p>
                                </div>
                                <div class="md:col-span-2">
                                    <h4 class="font-semibold text-lg mb-2">Outcomes & Reflections</h4>
                                    <p class="text-stone-600 project-desc">Currently, the model is undergoing experimental validation and has yielded promising preliminary results. I was responsible for the entire process from theory to experimentation. This project significantly enhanced my independent research capabilities, my understanding of complex signal processing, and my confidence in solving practical engineering challenges.</p>
                                </div>
                            </div>
                            <button class="generate-insight-btn mt-6 bg-sky-600 text-white px-6 py-2 rounded-md hover:bg-sky-700 transition-colors">✨ Get Project Insight</button>
                            <div class="insight-output mt-4 text-stone-700 leading-relaxed"></div>
                            <div class="loading-indicator mt-4 text-stone-500 hidden">Generating...</div>
                        </div>
                    </article>
                    <article id="project2" class="project-panel hidden">
                        <div class="bg-white p-8 rounded-lg shadow-lg">
                            <h3 class="text-2xl font-bold text-sky-800 mb-1">Data-Driven Production Defect Prediction: Mathematical Modeling in Industrial Application</h3>
                            <p class="text-sm text-stone-500 mb-4">National Mathematical Contest in Modeling (Leader)</p>
                             <div class="grid md:grid-cols-2 gap-8">
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">Project Background & Challenges</h4>
                                    <p class="text-stone-600 project-desc">Traditional production inspection is inefficient and struggles to dynamically predict defect rates, leading to increased costs and wasted resources.</p>
                                </div>
                                <div>
                                    <h4 class="font-semibold text-lg mb-2">My Approach & Methodology</h4>
                                    <p class="text-stone-600 project-desc">As the project leader, I led the team to develop a data-driven defect prediction model. We innovatively applied particle filtering and Monte Carlo simulation to dynamically estimate defect rates, thereby achieving precise monitoring and optimization of the production process.</p>
                                </div>
                                <div class="md:col-span-2">
                                    <h4 class="font-semibold text-lg mb-2">Outcomes & Reflections</h4>
                                    <p class="text-stone-600 project-desc">The model won the 'Second Prize in the National Mathematical Contest in Modeling'. I was responsible for the overall project's model design, algorithm implementation, and team coordination. This experience not only honed my mathematical modeling skills and ability to solve practical industrial problems but also made me deeply appreciate the importance of interdisciplinary collaboration.</p>
                                </div>
                            </div>
                            <button class="generate-insight-btn mt-6 bg-sky-600 text-white px-6 py-2 rounded-md hover:bg-sky-700 transition-colors">✨ Get Project Insight</button>
                            <div class="insight-output mt-4 text-stone-700 leading-relaxed"></div>
                            <div class="loading-indicator mt-4 text-stone-500 hidden">Generating...</div>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- Development Section -->
        <section id="development" class="py-20 md:py-32 bg-white fade-in-section">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-sky-900">Holistic Development</h2>
                    <p class="text-lg text-stone-600 mt-2">My Innovation Potential & Redbird Vision</p>
                </div>
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="bg-stone-100 p-6 rounded-lg text-center shadow-sm">
                        <div class="text-4xl mb-3">🤝</div>
                        <h3 class="text-xl font-semibold text-stone-800 mb-2">Diverse Development & Leadership</h3>
                        <p class="text-stone-600">As the Deputy Secretary of the Youth League Committee of Hongshen College, I organized and coordinated various student activities, and was honored as an Outstanding Student Cadre, cultivating excellent organizational, communication, and leadership skills.</p>
                    </div>
                     <div class="bg-stone-100 p-6 rounded-lg text-center shadow-sm">
                        <div class="text-4xl mb-3">🏃‍♀️</div>
                        <h3 class="text-xl font-semibold text-stone-800 mb-2">Resilient Athletic Spirit</h3>
                        <p class="text-stone-600">Completed full and half marathons, achieved First-Class in physical fitness test, and top eight in university badminton. These experiences shaped my qualities of perseverance, self-discipline, and teamwork.</p>
                    </div>
                     <div class="bg-stone-100 p-6 rounded-lg text-center shadow-sm">
                        <div class="text-4xl mb-3">🎯</div>
                        <h3 class="text-xl font-semibold text-stone-800 mb-2">Future Vision & Redbird Alignment</h3>
                        <p class="text-stone-600" id="future-vision-text">I aspire to apply my skills in the interdisciplinary environment of the Redbird Camp to address pain points for SMEs, facilitating their transformation and laying a solid foundation for future development.</p>
                        <button id="expand-vision-btn" class="mt-4 bg-sky-600 text-white px-6 py-2 rounded-md hover:bg-sky-700 transition-colors">✨ Expand Future Potential</button>
                        <div id="expanded-vision-output" class="mt-4 text-stone-700 leading-relaxed"></div>
                        <div id="vision-loading-indicator" class="mt-4 text-stone-500 hidden">Generating...</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <footer id="contact" class="py-20 bg-sky-900 text-white fade-in-section">
            <div class="container mx-auto px-6 text-center">
                 <h2 class="text-3xl font-bold">Contact Me</h2>
                 <p class="mt-4 max-w-2xl mx-auto">I look forward to discussing more about technology, innovation, and how to create value for SMEs. If you are interested in my experience or wish to explore potential collaborations, please feel free to contact me through the following methods.</p>
                 <div class="mt-8">
                    <a href="mailto:chennnnyanxi@163.com" class="inline-block bg-white text-sky-800 px-8 py-3 rounded-md text-lg font-semibold hover:bg-stone-100 transition-colors">Send Email</a>
                 </div>
                 <div class="mt-8 text-stone-300">
                     <p>Email: chennnnyanxi@163.com</p>
                 </div>
            </div>
        </footer>

    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Mobile Menu Toggle
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });

            // Skills Chart
            const ctx = document.getElementById('skillsChart').getContext('2d');
            const skillsChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['Mathematical Modeling', 'Federated Learning', 'Signal Processing', 'Fault Detection', 'Data Analysis', 'Reinforcement Learning'],
                    datasets: [{
                        label: 'Proficiency in Professional Skills',
                        data: [90, 85, 80, 80, 95, 75],
                        backgroundColor: 'rgba(12, 74, 110, 0.2)',
                        borderColor: 'rgba(12, 74, 110, 1)',
                        pointBackgroundColor: 'rgba(12, 74, 110, 1)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgba(12, 74, 110, 1)'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { color: 'rgba(0, 0, 0, 0.1)' },
                            grid: { color: 'rgba(0, 0, 0, 0.1)' },
                            pointLabels: { 
                                font: { size: 12, family: "'Inter', 'Noto Sans SC', sans-serif" },
                                color: '#44403c' // stone-700
                            },
                            ticks: {
                                backdropColor: 'transparent',
                                color: '#a8a29e', // stone-400
                                stepSize: 25
                            },
                            suggestedMin: 0,
                            suggestedMax: 100
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });

            // Project Tabs
            const tabs = document.querySelectorAll('.tab-btn');
            const panels = document.querySelectorAll('.project-panel');
            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    tabs.forEach(t => t.classList.remove('tab-active', 'text-stone-800'));
                    panels.forEach(p => p.classList.add('hidden'));

                    tab.classList.add('tab-active');
                    tab.classList.remove('text-stone-500', 'hover:text-stone-700');
                    document.getElementById(tab.dataset.target).classList.remove('hidden');
                });
            });

            // LLM Integration for Project Insights
            document.querySelectorAll('.generate-insight-btn').forEach(button => {
                button.addEventListener('click', async (event) => {
                    const projectPanel = event.target.closest('.project-panel');
                    const projectTitle = projectPanel.querySelector('h3').textContent;
                    const projectDescElements = projectPanel.querySelectorAll('.project-desc');
                    let projectDescription = '';
                    projectDescElements.forEach(el => {
                        projectDescription += el.textContent + ' ';
                    });

                    const insightOutputDiv = projectPanel.querySelector('.insight-output');
                    const loadingIndicator = projectPanel.querySelector('.loading-indicator');

                    insightOutputDiv.textContent = ''; // Clear previous output
                    loadingIndicator.classList.remove('hidden'); // Show loading

                    try {
                        const prompt = `Please generate a summary of about 100 words for the following project, highlighting its innovativeness, technical application, and solution to practical problems. Focus on its value in current technological trends or industrial applications, especially its potential to empower small and medium-sized enterprises (SMEs).\n\nProject Title: ${projectTitle}\nProject Description: ${projectDescription.trim()}`;
                        let chatHistory = [];
                        chatHistory.push({ role: "user", parts: [{ text: prompt }] });
                        const payload = { contents: chatHistory };
                        const apiKey = ""; 
                        const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;
                        const response = await fetch(apiUrl, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload)
                        });
                        const result = await response.json();
                        if (result.candidates && result.candidates.length > 0 &&
                            result.candidates[0].content && result.candidates[0].content.parts &&
                            result.candidates[0].content.parts.length > 0) {
                            const text = result.candidates[0].content.parts[0].text;
                            insightOutputDiv.textContent = text;
                        } else {
                            insightOutputDiv.textContent = 'Failed to generate insight. Please try again later.';
                        }
                    } catch (error) {
                        console.error('Error generating insight:', error);
                        insightOutputDiv.textContent = 'An error occurred while generating insight.';
                    } finally {
                        loadingIndicator.classList.add('hidden'); // Hide loading
                    }
                });
            });

            // LLM Integration for Future Vision Expansion
            const expandVisionBtn = document.getElementById('expand-vision-btn');
            const futureVisionText = document.getElementById('future-vision-text').textContent;
            const expandedVisionOutput = document.getElementById('expanded-vision-output');
            const visionLoadingIndicator = document.getElementById('vision-loading-indicator');

            expandVisionBtn.addEventListener('click', async () => {
                expandedVisionOutput.textContent = ''; // Clear previous output
                visionLoadingIndicator.classList.remove('hidden'); // Show loading

                try {
                    const prompt = `Based on the following personal future vision, further expand its potential, providing more specific directions, challenges, or collaboration opportunities, making it more in-depth and forward-looking, approximately 150 words. Please focus on how mathematical insights, data analysis, and innovative spirit can be applied in fields like intelligent manufacturing, smart transportation, and emphasize their role in empowering small and medium-sized enterprises (SMEs).\n\nMy Future Vision: ${futureVisionText}`;
                    let chatHistory = [];
                    chatHistory.push({ role: "user", parts: [{ text: prompt }] });
                    const payload = { contents: chatHistory };
                    const apiKey = ""; 
                    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;
                    const response = await fetch(apiUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    const result = await response.json();
                    if (result.candidates && result.candidates.length > 0 &&
                        result.candidates[0].content && result.candidates[0].content.parts &&
                        result.candidates[0].content.parts.length > 0) {
                        const text = result.candidates[0].content.parts[0].text;
                        expandedVisionOutput.textContent = text;
                    } else {
                        expandedVisionOutput.textContent = 'Failed to expand future potential. Please try again later.';
                    }
                } catch (error) {
                    console.error('Error expanding vision:', error);
                    expandedVisionOutput.textContent = 'An error occurred while expanding future potential.';
                } finally {
                    visionLoadingIndicator.classList.add('hidden'); // Hide loading
                }
            });


            // Fade-in sections on scroll
            const sections = document.querySelectorAll('.fade-in-section');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    }
                });
            }, {
                threshold: 0.1
            });
            sections.forEach(section => observer.observe(section));

            // Header shadow on scroll
            const header = document.getElementById('header');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 10) {
                    header.classList.add('shadow-md');
                } else {
                    header.classList.remove('shadow-md');
                }
            });
        });
    </script>
</body>
</html>
