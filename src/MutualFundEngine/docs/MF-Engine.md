::: mermaid
classDiagram
    class BaseSQLIdModel{
        <<Abstract>>
        +UUID Id
    }
    class AMCModel{
        +String Name
    }
    BaseSQLIdModel <|-- AMCModel
:::