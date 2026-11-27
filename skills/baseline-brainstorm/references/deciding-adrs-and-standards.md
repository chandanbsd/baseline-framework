# Deciding what to record

A conversation can settle a standard, an ADR, both, or neither.

## Standard

A blanket rule with very limited exceptions. State the end result, and add short mnemonic snippets where they help.

Example: "C# payloads and contracts are records, not classes."

```csharp
public sealed record CreateOrder(Guid CustomerId, IReadOnlyList<OrderLine> Lines);   // yes
public sealed class CreateOrderDto { public Guid CustomerId { get; set; } }          // no
```

Write one when the engineer says "always", "never", "from now on" or "every ..." about how code is written.

## ADR

A decision of impact: a new technology or dependency, a data model or public interface, a security or trust boundary, the deployment topology, or anything hard to reverse. State the decision as the desired output, then one or two lines of why. The alternatives and why-not go in the course, not here.

## Neither

A one-off choice that touches one place and is easy to change. Write no document for it.

## Telling them apart

| The engineer said | Record |
|---|---|
| "Every payload type is a record." | Standard |
| "We will use Postgres, not DynamoDB." | ADR |
| "Call that variable `total`." | Neither |

One decision per file. Write it from the `TEMPLATE.md` in `baseline/adr/` or `baseline/standards/`.
