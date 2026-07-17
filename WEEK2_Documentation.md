# Week 2 - AI Image Editing & Version History Documentation


## AI API Selection

The application is designed using Generative AI vision APIs for image understanding and editing.

Selected API:
- Google Gemini Vision API

Reason for Selection:
- Supports multimodal input (text + images)
- Provides image analysis capabilities
- Good integration with Python applications
- Suitable for natural language based image editing workflows


## Image Editing Workflow

User Input:

Example:
"Remove the person on the left and add a sunset background"


Flow:

User Prompt

↓

Streamlit Edit Interface

↓

Prompt Engineering Layer

↓

Vision AI API

↓

Generated Edited Image

↓

Version Storage

↓

History Display


## Prompt Engineering Strategy

Prompts are designed to provide clear instructions to the AI model.

Example:

User Request:
Remove background


AI Prompt Template:

"You are an AI image editing assistant.

Remove unwanted objects/background while preserving:
- Image quality
- Lighting
- Natural appearance
- Important subjects"


## Version History Implementation

Every edit operation creates a new version.

Stored information:

- Original image name
- Edited image name
- User prompt
- Timestamp


Example:

Original Image:

image.jpg


Edited Versions:

image_v1.jpg
image_v2.jpg
image_v3.jpg


## Benefits

- Users can track previous edits
- Original images remain unchanged
- Multiple editing attempts are supported
- Future AI model integration is easier


## Future Improvements

- Real AI image generation API integration
- Cloud storage
- Semantic image search
- User authentication
- Advanced editing controls