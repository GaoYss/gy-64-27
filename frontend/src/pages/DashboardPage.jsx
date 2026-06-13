import {
  Banknote,
  CalendarClock,
  CircleDollarSign,
  ClipboardList,
  TrendingUp,
  Wallet,
} from "lucide-react";

import { ProgressBar } from "../components/ProgressBar.jsx";
import { StatusBadge } from "../components/StatusBadge.jsx";
import { useAppData } from "../context/AppContext.jsx";

const metricIcons = [ClipboardList, CalendarClock, TrendingUp, CircleDollarSign];

export function DashboardPage() {
  const { dashboard } = useAppData();

  if (!dashboard) return null;

  const fin = dashboard.financial_summary;
  const financialMetrics = [
    {
      label: "Total Budget",
      value: `CNY ${Number(fin.total_budget).toLocaleString()}`,
      icon: Wallet,
      trend: `${dashboard.project_costs.length} projects`,
    },
    {
      label: "Procurement Cost",
      value: `CNY ${Number(fin.total_procurement).toLocaleString()}`,
      icon: CircleDollarSign,
      trend: "Material spend",
    },
    {
      label: "Payments Received",
      value: `CNY ${Number(fin.total_payments_received).toLocaleString()}`,
      icon: Banknote,
      trend: "Collected to date",
    },
    {
      label: "Gross Profit",
      value: `CNY ${Number(fin.total_gross_profit).toLocaleString()}`,
      icon: TrendingUp,
      trend: `${fin.overall_margin}% margin`,
    },
  ];

  return (
    <div className="page-stack">
      <section className="metric-grid">
        {dashboard.metrics.map((metric, index) => {
          const Icon = metricIcons[index] ?? TrendingUp;
          return (
            <article className="metric-card" key={metric.label}>
              <Icon size={20} />
              <span>{metric.label}</span>
              <strong>{metric.value}</strong>
              <small>{metric.trend}</small>
            </article>
          );
        })}
      </section>

      <section className="metric-grid">
        {financialMetrics.map((metric) => {
          const Icon = metric.icon;
          return (
            <article className="metric-card" key={metric.label}>
              <Icon size={20} />
              <span>{metric.label}</span>
              <strong>{metric.value}</strong>
              <small>{metric.trend}</small>
            </article>
          );
        })}
      </section>

      <section className="dashboard-grid">
        <div className="panel">
          <div className="section-heading">
            <h2>Construction Updates</h2>
            <span>Budget CNY {dashboard.procurement_budget.toLocaleString()}</span>
          </div>
          <div className="update-list">
            {dashboard.recent_updates.map((item) => (
              <article key={item.project_name} className="update-row">
                <div>
                  <strong>{item.project_name}</strong>
                  <p>{item.latest_update}</p>
                </div>
                <StatusBadge value={item.phase} />
                <ProgressBar value={item.progress} />
              </article>
            ))}
          </div>
        </div>
        <div className="panel">
          <div className="section-heading">
            <h2>Phase Load</h2>
            <span>{new Date(dashboard.generated_at).toLocaleString()}</span>
          </div>
          <div className="phase-list">
            {dashboard.phase_distribution.map((item) => (
              <div key={item.phase} className="phase-row">
                <span>{item.phase}</span>
                <strong>{item.count}</strong>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="panel">
        <div className="section-heading">
          <h2>Project Profitability</h2>
          <span>Overall margin {fin.overall_margin}%</span>
        </div>
        <div className="update-list">
          {dashboard.project_costs.map((item) => (
            <article key={item.project_id} className="update-row">
              <div>
                <strong>{item.project_name}</strong>
                <p>
                  Budget CNY {Number(item.budget).toLocaleString()} | Procurement CNY{" "}
                  {Number(item.procurement_total).toLocaleString()} | Received CNY{" "}
                  {Number(item.payment_received).toLocaleString()}
                </p>
              </div>
              <strong
                style={{ color: item.gross_profit >= 0 ? "#16a34a" : "#dc2626" }}
              >
                CNY {Number(item.gross_profit).toLocaleString()}
              </strong>
              <span style={{ color: item.gross_margin >= 0 ? "#16a34a" : "#dc2626" }}>
                {item.gross_margin}%
              </span>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
