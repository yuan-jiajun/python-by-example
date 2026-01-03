const documentation = [
    {
        id: "01_basics",
        title: "01. Python Basics",
        description: "Fundamental syntax and data types.",
        icon: "fas fa-seedling",
        lessons: [
            { title: "Print Function", file: "01_basics/01_print.py" },
            { title: "Comments", file: "01_basics/02_comments.py" },
            { title: "Variables", file: "01_basics/03_variables.py" },
            { title: "Data Types", file: "01_basics/04_data_types.py" }
        ]
    },
    {
        id: "02_control_flow",
        title: "02. Control Flow",
        description: "Conditional logic and selection.",
        icon: "fas fa-code-branch",
        lessons: [
            { title: "If-Else", file: "02_control_flow/01_if_else.py" },
            { title: "Elif", file: "02_control_flow/02_elif.py" },
            { title: "Match Case", file: "02_control_flow/03_match_case.py" }
        ]
    },
    {
        id: "03_loops",
        title: "03. Loops & Iterations",
        description: "Repetitive task automation.",
        icon: "fas fa-sync",
        lessons: [
            { title: "For Loops", file: "03_loops/01_for_loop.py" },
            { title: "While Loops", file: "03_loops/02_while_loop.py" },
            { title: "Break & Continue", file: "03_loops/03_break_continue.py" }
        ]
    },
    {
        id: "04_data_structures",
        title: "04. Data Structures",
        description: "Collections and data management.",
        icon: "fas fa-database",
        lessons: [
            { title: "Lists", file: "04_data_structures/01_lists.py" },
            { title: "Tuples", file: "04_data_structures/02_tuples.py" },
            { title: "Sets", file: "04_data_structures/03_sets.py" },
            { title: "Dictionaries", file: "04_data_structures/04_dictionaries.py" }
        ]
    },
    {
        id: "05_functions",
        title: "05. Functions",
        description: "Modular and reusable blocks.",
        icon: "fas fa-cube",
        lessons: [
            { title: "Function Basics", file: "05_functions/01_function_basics.py" },
            { title: "Arguments", file: "05_functions/02_arguments.py" },
            { title: "Return Values", file: "05_functions/03_return_values.py" },
            { title: "Lambda Functions", file: "05_functions/04_lambda_functions.py" }
        ]
    },
    {
        id: "06_modules_packages",
        title: "06. Modules & Packages",
        description: "Code organization and imports.",
        icon: "fas fa-box-open",
        lessons: [
            { title: "Imports", file: "06_modules_packages/01_imports.py" },
            { title: "Custom Modules", file: "06_modules_packages/02_custom_modules.py" }
        ]
    },
    {
        id: "07_error_handling",
        title: "07. Error Handling",
        description: "Robustness and exception safety.",
        icon: "fas fa-exclamation-triangle",
        lessons: [
            { title: "Try-Except", file: "07_error_handling/01_try_except.py" },
            { title: "Custom Exceptions", file: "07_error_handling/02_custom_exceptions.py" }
        ]
    },
    {
        id: "08_oop",
        title: "08. Object Oriented Programming",
        description: "Classes, objects, and inheritance.",
        icon: "fas fa-project-diagram",
        lessons: [
            { title: "Classes & Objects", file: "08_oop/01_classes_objects.py" },
            { title: "Init Methods", file: "08_oop/02_init_methods.py" },
            { title: "Inheritance", file: "08_oop/03_inheritance.py" },
            { title: "Polymorphism", file: "08_oop/04_polymorphism.py" }
        ]
    },
    {
        id: "09_advanced_python",
        title: "09. Advanced Python",
        description: "Generators, decorators, and more.",
        icon: "fas fa-bolt",
        lessons: [
            { title: "List Comprehensions", file: "09_advanced_python/01_list_comprehensions.py" },
            { title: "Generators", file: "09_advanced_python/02_generators.py" },
            { title: "Decorators", file: "09_advanced_python/03_decorators.py" },
            { title: "Context Managers", file: "09_advanced_python/04_context_managers.py" }
        ]
    },
    {
        id: "10_best_practices",
        title: "10. Best Practices",
        description: "Clean code and professional PEP 8.",
        icon: "fas fa-check-double",
        lessons: [
            { title: "PEP 8", file: "10_best_practices/01_pep8.py" },
            { title: "Type Hinting", file: "10_best_practices/02_type_hinting.py" },
            { title: "Virtual Envs", file: "10_best_practices/03_virtual_envs.py" }
        ]
    }
];

let pyodideInstance = null;
let editor = null;
let originalCode = "";

// Initialize Monaco Editor
require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs' } });
require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('monaco-editor-container'), {
        value: "# Select a lesson to begin...",
        language: 'python',
        theme: 'vs-dark',
        automaticLayout: true,
        readOnly: true,
        fontSize: 14,
        minimap: { enabled: false },
        lineNumbers: 'on',
        scrollBeyondLastLine: false,
        padding: { top: 20 }
    });
});

async function initPyodide() {
    const outputArea = document.getElementById('output-area');
    try {
        pyodideInstance = await loadPyodide();
        outputArea.textContent = ">>> Python 3.10 (Pyodide) Ready.\n";
        document.getElementById('run-btn').disabled = false;
    } catch (err) {
        outputArea.textContent = "Error loading Pyodide: " + err.message;
    }
}

async function runPython(code) {
    const outputArea = document.getElementById('output-area');

    if (!pyodideInstance) {
        outputArea.textContent = ">>> Error: Python environment not yet initialized. Please wait.\n";
        return;
    }

    outputArea.textContent = "Running...\n";

    try {
        pyodideInstance.setStdout({
            batched: (text) => {
                outputArea.textContent += text + "\n";
            }
        });

        await pyodideInstance.runPythonAsync(code);
        outputArea.textContent += "\n[Execution Complete]";
    } catch (err) {
        outputArea.textContent += "\nTraceback (most recent call last):\n" + err.message;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initPyodide();

    const content = document.getElementById('documentation-content');
    const toc = document.getElementById('toc');
    const modal = document.getElementById('playground-modal');
    const lessonTitle = document.getElementById('lesson-title');
    const resetBtn = document.getElementById('reset-btn');
    const editBtn = document.getElementById('edit-btn');
    const runBtn = document.getElementById('run-btn');
    const closeModal = document.querySelector('.close-modal');

    content.innerHTML = '';
    toc.innerHTML = '';

    // Render Documentation
    documentation.forEach((module) => {
        const section = document.createElement('section');
        section.id = module.id;
        section.className = 'doc-section';

        section.innerHTML = `
            <h2><i class="${module.icon || 'fas fa-book'}" style="margin-right: 12px; font-size: 1.2rem; color: var(--accent);"></i>${module.title}</h2>
            <p>${module.description}</p>
            <div class="module-card">
                <ul class="lesson-list" style="list-style: none; padding-left: 0;">
                    ${module.lessons.map(lesson => `
                        <li class="lesson-item" data-file="${lesson.file}" data-title="${lesson.title}" 
                            style="padding: 12px; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: 0.2s; border-radius: 6px;">
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <i class="fab fa-python" style="color: var(--accent);"></i>
                                <span>${lesson.title}</span>
                            </div>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Run Live <i class="fas fa-play" style="font-size: 0.6rem;"></i></span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `;
        content.appendChild(section);

        const tocLink = document.createElement('a');
        tocLink.href = `#${module.id}`;
        tocLink.className = 'toc-link';
        tocLink.textContent = module.title;
        toc.appendChild(tocLink);
    });

    // Handle Lesson Clicks
    document.addEventListener('click', async (e) => {
        const item = e.target.closest('.lesson-item');
        if (!item) return;

        const file = item.getAttribute('data-file');
        const title = item.getAttribute('data-title');
        lessonTitle.textContent = `${title}.py`;
        modal.classList.add('active');

        // Monaco needs layout() called when container becomes visible to display cursor/suggestions correctly
        setTimeout(() => {
            if (editor) {
                editor.layout();
                editor.focus();
            }
        }, 100);

        // Reset edit mode
        editBtn.classList.remove('active');
        editBtn.innerHTML = '<i class="fas fa-edit"></i> Edit';
        if (editor) editor.updateOptions({ readOnly: true });

        if (editor) editor.setValue("# Loading source code...");

        try {
            const response = await fetch(file);
            if (!response.ok) throw new Error("File not found");
            const code = await response.text();
            originalCode = code;
            if (editor) {
                editor.setValue(code);
                // Force suggestions/intellisense refresh
                monaco.editor.setModelLanguage(editor.getModel(), 'python');
            }
        } catch (err) {
            const fallback = `# Error loading file: ${file}\n# serving from github.io might require valid paths.\n\nprint("Hello from Python By Example!")\nname = "Developer"\nprint(f"Happy coding, {name}!")`;
            originalCode = fallback;
            if (editor) editor.setValue(fallback);
        }
    });

    // Edit Toggle
    editBtn.addEventListener('click', () => {
        if (!editor) return;
        const isEditing = editBtn.classList.toggle('active');
        editor.updateOptions({ readOnly: !isEditing });

        if (isEditing) {
            editBtn.innerHTML = '<i class="fas fa-check"></i> Editing...';
            editor.focus();
            document.getElementById('output-area').textContent = ">>> Editing mode enabled. You can now modify the code and see suggestions.\n";
        } else {
            editBtn.innerHTML = '<i class="fas fa-edit"></i> Edit';
            document.getElementById('output-area').textContent = ">>> Editing mode disabled.\n";
        }
    });

    // Reset Logic
    resetBtn.addEventListener('click', () => {
        if (!editor) return;
        editor.setValue(originalCode);
        editBtn.classList.remove('active');
        editor.updateOptions({ readOnly: true });
        editBtn.innerHTML = '<i class="fas fa-edit"></i> Edit';
        document.getElementById('output-area').textContent = ">>> Code reset to original state.\n";
    });

    // Run Logic
    runBtn.addEventListener('click', () => {
        if (editor) runPython(editor.getValue());
    });

    // Modal Controls
    closeModal.addEventListener('click', () => modal.classList.remove('active'));
    modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('active');
    });

    // Search Functionality (Improved)
    const searchInput = document.querySelector('.search-box input');
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();

        document.querySelectorAll('.doc-section').forEach(section => {
            const heading = section.querySelector('h2').textContent.toLowerCase();
            const desc = section.querySelector('p').textContent.toLowerCase();
            const lessonItems = section.querySelectorAll('.lesson-item');

            let isSectionVisible = query === "" || heading.includes(query) || desc.includes(query);
            let matchingLessonsCount = 0;

            lessonItems.forEach(item => {
                const lessonText = item.textContent.toLowerCase();
                const isLessonMatch = query === "" || lessonText.includes(query);

                // Show lesson if it matches or if the section title matches
                const shouldShowLesson = isSectionVisible || isLessonMatch;
                item.style.setProperty('display', shouldShowLesson ? 'flex' : 'none', 'important');

                if (isLessonMatch) matchingLessonsCount++;
            });

            // Show section if title matches or if any lesson inside matches
            section.style.display = (isSectionVisible || matchingLessonsCount > 0) ? 'block' : 'none';
        });

        // Sync TOC
        document.querySelectorAll('.toc-link').forEach(link => {
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                link.style.display = targetSection.style.display === 'none' ? 'none' : 'block';
            }
        });
    });

    // Scroll Spy
    window.addEventListener('scroll', () => {
        let current = '';
        document.querySelectorAll('.doc-section').forEach(section => {
            if (section.style.display !== 'none' && window.pageYOffset >= (section.offsetTop - 150)) {
                current = section.getAttribute('id');
            }
        });
        document.querySelectorAll('.toc-link').forEach(link => {
            link.classList.remove('active');
            if (link.style.display !== 'none' && link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });
});
