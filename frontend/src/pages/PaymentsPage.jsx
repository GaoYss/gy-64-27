import { DataTable } from "../components/DataTable.jsx";
import { RecordForm } from "../components/RecordForm.jsx";
import { StatusBadge } from "../components/StatusBadge.jsx";
import { useAppData } from "../context/AppContext.jsx";
import { paymentFields } from "../modules/forms.js";

const columns = [
  { key: "project_name", label: "Project" },
  { key: "amount", label: "Amount", render: (row) => `CNY ${Number(row.amount).toLocaleString()}` },
  { key: "payment_date", label: "Payment date" },
  { key: "status", label: "Status", render: (row) => <StatusBadge value={row.status} /> },
  { key: "notes", label: "Notes" },
];

export function PaymentsPage() {
  const { payments, createRecord } = useAppData();
  const totalReceived = payments
    .filter((p) => p.status === "received")
    .reduce((sum, item) => sum + Number(item.amount), 0);
  const totalPending = payments
    .filter((p) => p.status === "pending" || p.status === "partial")
    .reduce((sum, item) => sum + Number(item.amount), 0);

  return (
    <div className="page-stack">
      <RecordForm
        title="Record payment"
        fields={paymentFields}
        onSubmit={(payload) => createRecord("payments", payload)}
      />
      <section className="panel">
        <div className="section-heading">
          <h2>Payment Collection</h2>
          <span>
            Received CNY {totalReceived.toLocaleString()} / Pending CNY {totalPending.toLocaleString()}
          </span>
        </div>
        <DataTable columns={columns} rows={payments} />
      </section>
    </div>
  );
}
