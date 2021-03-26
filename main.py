import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

fmri = sns.load_dataset("fmri")

sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            dashes=False, markers=True, kind="line", data=fmri)
plt.show()
