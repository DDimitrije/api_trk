"""empty message

Revision ID: 863c68d7537b
Revises: 
Create Date: 2023-08-25 14:04:54.726814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863c68d7537b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manifestacijas',
    sa.Column('id_manifestacija', sa.Integer(), nullable=False),
    sa.Column('imeManifestacija', sa.String(length=150), nullable=False),
    sa.Column('datum', sa.String(length=80), nullable=False),
    sa.Column('vremeStarta', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id_manifestacija'),
    sa.UniqueConstraint('datum'),
    sa.UniqueConstraint('imeManifestacija'),
    sa.UniqueConstraint('vremeStarta')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('trkas',
    sa.Column('id_trka', sa.Integer(), nullable=False),
    sa.Column('nazivTrka', sa.String(length=80), nullable=False),
    sa.Column('startTrka', sa.String(length=80), nullable=False),
    sa.Column('krajTrka', sa.String(length=80), nullable=False),
    sa.Column('storno', sa.String(length=80), nullable=False),
    sa.Column('manifestacija_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['manifestacija_id'], ['manifestacijas.id_manifestacija'], ),
    sa.PrimaryKeyConstraint('id_trka')
    )
    op.create_table('androids',
    sa.Column('id_android', sa.Integer(), nullable=False),
    sa.Column('bib_android', sa.String(length=150), nullable=False),
    sa.Column('pozicija_android', sa.String(length=80), nullable=False),
    sa.Column('tag_code_android', sa.String(length=80), nullable=False),
    sa.Column('vreme_sistemsko_android', sa.String(length=80), nullable=False),
    sa.Column('storno_android', sa.String(length=80), nullable=False),
    sa.Column('trka_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trka_id'], ['trkas.id_trka'], ),
    sa.PrimaryKeyConstraint('id_android'),
    sa.UniqueConstraint('bib_android'),
    sa.UniqueConstraint('pozicija_android'),
    sa.UniqueConstraint('storno_android'),
    sa.UniqueConstraint('tag_code_android'),
    sa.UniqueConstraint('vreme_sistemsko_android')
    )
    op.create_table('citacs',
    sa.Column('id_citac', sa.Integer(), nullable=False),
    sa.Column('bib_citac', sa.String(length=150), nullable=False),
    sa.Column('ime_preziem_citac', sa.String(length=80), nullable=False),
    sa.Column('age_group_citac', sa.String(length=80), nullable=False),
    sa.Column('age_gun_time', sa.String(length=80), nullable=False),
    sa.Column('age_net_time', sa.String(length=80), nullable=False),
    sa.Column('age_storno', sa.String(length=80), nullable=False),
    sa.Column('trka_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trka_id'], ['trkas.id_trka'], ),
    sa.PrimaryKeyConstraint('id_citac'),
    sa.UniqueConstraint('age_group_citac'),
    sa.UniqueConstraint('age_gun_time'),
    sa.UniqueConstraint('age_net_time'),
    sa.UniqueConstraint('age_storno'),
    sa.UniqueConstraint('bib_citac'),
    sa.UniqueConstraint('ime_preziem_citac')
    )
    op.create_table('negativni_poenis',
    sa.Column('id_negativni', sa.Integer(), nullable=False),
    sa.Column('pozicija_negativni', sa.String(length=150), nullable=False),
    sa.Column('broj_poena_negativni', sa.String(length=80), nullable=False),
    sa.Column('kazna_sec_negativni', sa.String(length=80), nullable=False),
    sa.Column('storno_negativni', sa.String(length=80), nullable=False),
    sa.Column('trka_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trka_id'], ['trkas.id_trka'], ),
    sa.PrimaryKeyConstraint('id_negativni'),
    sa.UniqueConstraint('broj_poena_negativni'),
    sa.UniqueConstraint('kazna_sec_negativni'),
    sa.UniqueConstraint('pozicija_negativni'),
    sa.UniqueConstraint('storno_negativni')
    )
    op.create_table('trkacs',
    sa.Column('id_trkac', sa.Integer(), nullable=False),
    sa.Column('bib', sa.String(length=80), nullable=False),
    sa.Column('tagCode', sa.String(length=80), nullable=False),
    sa.Column('imePrezime', sa.String(length=80), nullable=False),
    sa.Column('godinaRodjenja', sa.String(length=80), nullable=False),
    sa.Column('mestoStanovanja', sa.String(length=80), nullable=False),
    sa.Column('drzava', sa.String(length=80), nullable=False),
    sa.Column('klub', sa.String(length=80), nullable=False),
    sa.Column('starosnaKategorija', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('smsBroj', sa.String(length=80), nullable=False),
    sa.Column('storno', sa.String(length=80), nullable=False),
    sa.Column('trka_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trka_id'], ['trkas.id_trka'], ),
    sa.PrimaryKeyConstraint('id_trkac'),
    sa.UniqueConstraint('bib')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trkacs')
    op.drop_table('negativni_poenis')
    op.drop_table('citacs')
    op.drop_table('androids')
    op.drop_table('trkas')
    op.drop_table('users')
    op.drop_table('manifestacijas')
    # ### end Alembic commands ###
