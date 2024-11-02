# DK Academy (Dream Library Academy)

DK Academy is an innovative educational tool designed to make learning fun and engaging for elementary students. By generating personalized comic books based on each student's interests and the topics they are studying, this platform transforms traditional learning into an interactive, visually rich experience. Subjects like mathematics come to life through storytelling, making them more relatable and enjoyable for young learners.

## Key Features

- **Personalized Comic Generation**: Tailors each comic book to the student's age, interests, and learning topic, providing a customized educational experience.
- **Interactive Learning**: Every comic panel includes a story, visuals, and a question, encouraging students to actively participate in their own learning.
- **Visual Content**: Leverages the **SDXL Lightning model** to generate high-quality images for the comic panels, enriching the visual experience.
- **Text Generation**: Uses **Google's Gemini model** to create personalized stories, questions, and explanations, ensuring the content is relevant to the student's learning journey.
- **User-Friendly Web Interface**: Built with **Streamlit**, offering a simple and intuitive way for users to input student data and view the generated comic.

## How It Works

1. The student’s information is entered, including their name, age, gender, interests, and the learning topic.
2. The AI generates a JSON structure containing the personalized comic book.
3. Each comic consists of multiple panels, with two visuals per panel, a story, and interactive questions that relate to the learning topic.
4. The student engages with the subject by following the story and answering questions embedded within the narrative.

## Technologies Used

- **Google Gemini Model**: Powers the generation of personalized stories, questions, and educational content.
- **SDXL Lightning Model**: Used to quickly generate high-quality images for each comic panel.
- **Streamlit**: Provides a clean and user-friendly web interface for generating and viewing the personalized comics.

## System Requirements

This project requires **NVIDIA CUDA** to run. Ensure you have CUDA version 12.1 installed. You can check your CUDA version using the following commands:

```bash
nvcc --version
```
or
```bash
nvidia-smi
```

### Installing CUDA

If CUDA is not installed on your system, you can download it from the official NVIDIA website. Follow the instructions provided in the link below to install the correct version:

[NVIDIA CUDA 12.1 Toolkit Download](https://developer.nvidia.com/cuda-12-1-0-download-archive)

## Installation Instructions

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/emretuncer256/dk-academy.git
   ```

2. Navigate to the project directory:
   ```bash
   cd dk-academy
   ```

3. Install the dependencies using Poetry:
   ```bash
   poetry install
   ```

4. Start the Streamlit application:
   ```bash
   poetry run streamlit run ./dkacademy/main.py
   ```

### First-Time Setup

Please note that the initial run may take a little longer as the necessary models will be downloaded from Hugging Face.

## Upcoming Features

- **Faster Image Generation**: To improve performance, image generation will be moved to an external API, significantly reducing generation time.
- **Voice Narration**: Integration of an AI model to provide voice narration for the stories, enhancing the learning experience.
- **AI-Generated Audio**: Tailored background music and sound effects related to the student's interests, created by AI to make the experience more immersive.