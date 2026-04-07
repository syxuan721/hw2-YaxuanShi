## Report

### Business Use Case

The workflow I built focuses on generating follow-up emails after meetings. This is a common task in business settings, especially for marketing, consulting, and project teams. Writing these emails manually takes time and effort, and the quality can vary depending on the person. Therefore, using a language model to automate this task can improve efficiency and consistency.

The system takes meeting notes as input and generates a follow-up email that summarizes key points and next steps. This is useful because it reduces repetitive writing work and helps ensure that important information is clearly communicated.

---

### Model Choice

I used a general-purpose large language model (GPT-based model) because it performs well on text generation tasks, especially for business writing. I did not test multiple models in this project, but based on prior experience and documentation, this type of model is suitable for generating structured and professional emails.

---

### Baseline vs Final Design

In the initial version, the prompt was simple and only described the general task. The output was mostly correct in terms of content, but there were some issues. For example, the model sometimes added a subject line or used bullet points, which were not required. The tone was also slightly generic.

After revising the prompt, I added more specific instructions to control formatting, such as removing subject lines and avoiding bullet points. This made the output more consistent and aligned with expectations.

In the final version, I further improved the prompt by asking the model to sound more natural and less generic. As a result, the email became more readable and closer to how a human would write it. Overall, prompt iteration clearly improved both formatting and tone.

---

### Limitations and Need for Human Review

Although the system works well for basic cases, it still has limitations. For example, if the input notes are incomplete or unclear, the model may generate vague or overly general content. It may also miss subtle context or produce text that sounds correct but is not fully accurate.

Because of this, human review is still necessary, especially in professional settings where accuracy matters. The system should be used as a draft generator rather than a final output tool.

---

### Deployment Recommendation

I would recommend deploying this workflow as a support tool rather than a fully automated system. It works well for generating first drafts of follow-up emails, which can then be reviewed and edited by users.

This workflow is most useful in situations where speed and consistency are important, but human oversight is still available. For example, it can be used by teams that regularly send follow-up emails after meetings.

However, it should not be used without review in high-stakes situations, such as client communication involving sensitive information. In those cases, additional checks are necessary to ensure accuracy and professionalism.
