from enum import Enum
from typing import Optional

from pydantic import BaseModel


class VerificationStatus(str, Enum):
    """
    Result of verifying a claim
    against retrieved document evidence.
    """

    SUPPORTED = "SUPPORTED"

    CONTRADICTED = "CONTRADICTED"

    INSUFFICIENT_EVIDENCE = (
        "INSUFFICIENT_EVIDENCE"
    )


class Claim(BaseModel):
    """
    One factual statement
    extracted from an answer.
    """

    claim_index: int

    text: str


class ClaimVerdict(BaseModel):
    """
    Verification result
    for one claim.
    """

    claim: Claim

    status: VerificationStatus

    confidence_score: float

    best_evidence_text: str

    evidence_page: Optional[int] = None

    contradiction_detail: Optional[str] = None


class HallucinationReport(BaseModel):
    """
    Final report
    for one answering system.
    """

    system_name: str

    answer: str

    total_claims: int

    supported_count: int

    contradicted_count: int

    insufficient_count: int

    hallucination_score: float

    is_reliable: bool

    reliability_label: str

    verdicts: list[ClaimVerdict]

    summary: str


class ComparisonReport(BaseModel):
    """
    Final comparison
    between RAG and Gemini.
    """

    question: str

    document_name: str

    rag_report: HallucinationReport

    gemini_report: HallucinationReport

    winner: str

    score_difference: float

    rag_is_more_reliable: bool

    comparison_summary: str


class VerificationResult(BaseModel):
    """
    Internal object passed
    between hallucination pipeline stages.
    """

    question: str

    document_name: str

    retrieved_chunks: list

    extracted_claims: list[Claim]

    hallucination_report: Optional[
        HallucinationReport
    ] = None