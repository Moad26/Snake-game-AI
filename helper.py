import matplotlib.pyplot as plt
from IPython import display

""" plt.ion()
 """
def plot(scores, mean_scores, update_freq=5):
    """Plots training progress, updating less frequently for better performance."""
    if len(scores) % update_freq == 0:  # Update only every 'update_freq' steps
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.clf()
        plt.title('Training Progress')
        plt.xlabel('Number of Games')
        plt.ylabel('Score')
        plt.plot(scores, label='Score', color='blue')
        plt.plot(mean_scores, label='Mean Score', color='red')
        plt.ylim(ymin=0)
        plt.legend()
        plt.text(len(scores)-1, scores[-1], str(scores[-1]))
        plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
        plt.show(block=False)
        plt.pause(0.1)  # Small pause to allow updates