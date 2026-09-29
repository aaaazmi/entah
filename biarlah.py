import matplotlib.pyplot as plt

quarterly = {"Q1'26": 1427, "Q2'26": 1674, "Q3'26": 264}
monthly = {
    "Jan'26": 102, "Feb'26": 1177, "Mar'26": 148, "Apr'26": 1287,
    "May'26": 195, "Jun'26": 220, "Jul'26": 107, "Aug'26": 79, "Sep'26": 50
}
weekly = {"WW35": 3, "WW36": 13, "WW37": 27, "WW38": 10}

fig = plt.figure(figsize=(16, 8.8))
gs = fig.add_gridspec(2, 2, hspace=0.14, wspace=0.08)

# Main title
fig.suptitle(
    "RMS APPROVAL — TREND DASHBOARD (Quarterly → Monthly → Weekly Drill-Down)",
    fontsize=16, fontweight="bold", y=0.98
)
fig.text(
    0.5, 0.955,
    "Data as of 8-Sep-2026  |  Analysis: Quarterly vs Monthly vs Weekly drill-down",
    ha="center", fontsize=9, style="italic"
)

def add_bar_labels(ax, bars):
    for b in bars:
        ax.text(
            b.get_x() + b.get_width()/2, b.get_height() + max(b.get_height()*0.025, 2),
            f"{int(b.get_height()):,}", ha="center", va="bottom", fontsize=9
        )

def panel(ax, title):
    ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
    ax.grid(axis="y", alpha=0.15)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_alpha(0.25)

# Quarterly
ax1 = fig.add_subplot(gs[0, 0])
bars = ax1.bar(quarterly.keys(), quarterly.values(), width=0.5)
panel(ax1, "RMS Approval — Quarterly Trend")
ax1.set_ylabel("Count")
ax1.set_ylim(0, 1800)
add_bar_labels(ax1, bars)

# Monthly
ax2 = fig.add_subplot(gs[0, 1])
bars = ax2.bar(monthly.keys(), monthly.values(), width=0.55)
panel(ax2, "RMS Approval — Monthly Trend")
ax2.set_ylabel("Count")
ax2.set_ylim(0, 1400)
ax2.tick_params(axis="x", rotation=0, labelsize=8)
add_bar_labels(ax2, bars)

# Weekly
ax3 = fig.add_subplot(gs[1, 0])
bars = ax3.bar(weekly.keys(), weekly.values(), width=0.5)
panel(ax3, "RMS Approval — Weekly Trend")
ax3.set_ylabel("Count")
ax3.set_ylim(0, 30)
add_bar_labels(ax3, bars)

# Combined drill-down
ax4 = fig.add_subplot(gs[1, 1])
panel(ax4, "RMS Approval — Quarterly / Monthly / WW")
ax4.set_ylabel("Feedback count")

# Use three visually separated groups on one axis
xq = [0, 1, 2]
xm = [4, 5, 6, 7, 8, 9, 10, 11, 12]
xw = [14, 15, 16, 17]

bq = ax4.bar(xq, list(quarterly.values()), width=0.55)
bm = ax4.bar(xm, list(monthly.values()), width=0.55)
bw = ax4.bar(xw, list(weekly.values()), width=0.55)

add_bar_labels(ax4, bq)
add_bar_labels(ax4, bm)
add_bar_labels(ax4, bw)

ax4.set_ylim(0, 1800)
ax4.set_xticks(xq + xm + xw)
ax4.set_xticklabels(
    list(quarterly.keys()) + list(monthly.keys()) + list(weekly.keys()),
    fontsize=7, rotation=0
)

# Clean dashboard look
fig.patch.set_facecolor("white")
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_facecolor("white")

plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.93])
plt.savefig("rms_approval_dashboard.png", dpi=180, bbox_inches="tight")
plt.show()
