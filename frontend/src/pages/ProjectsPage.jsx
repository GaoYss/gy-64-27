import { DataTable } from "../components/DataTable.jsx";
import { ProgressBar } from "../components/ProgressBar.jsx";
import { RecordForm } from "../components/RecordForm.jsx";
import { StatusBadge } from "../components/StatusBadge.jsx";
import { useAppData } from "../context/AppContext.jsx";
import { projectFields } from "../modules/forms.js";

const columns = [
  { key: "project_name", label: "Project" },
  { key: "customer_name", label: "Customer" },
  { key: "manager", label: "Manager" },
  { key: "phase", label: "Phase", render: (row) => <StatusBadge value={row.phase} /> },
  { key: "progress", label: "Progress", render: (row) => <ProgressBar value={row.progress} /> },
  { key: "risk_level", label: "Risk", render: (row) => <StatusBadge value={row.risk_level} /> },
  { key: "budget", label: "Budget", render: (row) => `CNY ${Number(row.budget).toLocaleString()}` },
  { key: "expected_finish", label: "Finish" },
  { key: "latest_update", label: "Latest update" },
];

const costColumns = [
  { key: "project_name", label: "Project" },
  { key: "customer_name", label: "Customer" },
  { key: "budget", label: "Budget", render: (row) => `CNY ${Number(row.budget).toLocaleString()}` },
  {
    key: "procurement_total",
    label: "Procurement Cost",
    render: (row) => `CNY ${Number(row.procurement_total).toLocaleString()}`,
  },
  {
    key: "payment_received",
    label: "Payments Received",
    render: (row) => `CNY ${Number(row.payment_received).toLocaleString()}`,
  },
  {
    key: "gross_profit",
    label: "Gross Profit",
    render: (row) => (
      <strong style={{ color: row.gross_profit >= 0 ? "#16a34a" : "#dc2626" }}>
        CNY {Number(row.gross_profit).toLocaleString()}
      </strong>
    ),
  },
  {
    key: "gross_margin",
    label: "Margin",
    render: (row) => (
      <span style={{ color: row.gross_margin >= 0 ? "#16a34a" : "#dc2626" }}>
        {row.gross_margin}%
      </span>
    ),
  },
];

export function ProjectsPage() {
  const { projects, projectCosts, createRecord } = useAppData();

  const totalBudget = projectCosts.reduce((sum, item) => sum + Number(item.budget), 0);
  const totalProcurement = projectCosts.reduce((sum, item) => sum + Number(item.procurement_total), 0);
  const totalPayments = projectCosts.reduce((sum, item) => sum + Number(item.payment_received), 0);
  const totalGrossProfit = totalBudget - totalProcurement;
  const overallMargin = totalBudget > 0 ? ((totalGrossProfit / totalBudget) * 100).toFixed(2) : 0;

  return (
    <div className="page-stack">
      <RecordForm title="Create project" fields={projectFields} onSubmit={(payload) => createRecord("projects", payload)} />
      <section className="panel">
        <div className="section-heading">
          <h2>Construction Progress</h2>
          <span>{projects.filter((project) => project.progress < 100).length} active</span>
        </div>
        <DataTable columns={columns} rows={projects} />
      </section>
      <section className="panel">
        <div className="section-heading">
          <h2>Project Cost Summary & Gross Profit</h2>
          <span>
            Margin {overallMargin}% | Profit CNY {totalGrossProfit.toLocaleString()} | Received CNY{" "}
            {totalPayments.toLocaleString()}
          </span>
        </div>
        <DataTable columns={costColumns} rows={projectCosts} />
      </section>
    </div>
  );
}
